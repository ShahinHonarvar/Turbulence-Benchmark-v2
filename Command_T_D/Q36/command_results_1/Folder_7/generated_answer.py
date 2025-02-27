import re

def filter_chars(str1):
    return re.sub('([A-Z][a-z]*)W([A-Z][a-z]*)y', '\x01X\x02', str1)