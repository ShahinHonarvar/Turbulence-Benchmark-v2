import re

def filter_chars(s):
    return re.sub('(.)\\d{4}(L)', '\x01', s)