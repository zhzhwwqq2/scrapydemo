# -*- coding: utf-8 -*-
import scrapy
from scrapydemo.items import ScrapydemoItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item = ScrapydemoItem()
        item['title'] = response.xpath('/html/head/title/text()').extract()
        yield item
