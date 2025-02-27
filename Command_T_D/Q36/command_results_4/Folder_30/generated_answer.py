import re

def filter_chars(string):
    return re.sub('([^3][^I]{%d}[^3][^I]{%d})', '', string)