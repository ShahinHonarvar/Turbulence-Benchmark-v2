import re

def filter_chars(str1):
    return re.sub('([A-z]+)([B-r]+)', '\x01', str1)