import re

def filter_chars(s):
    return re.sub('([\\d|a|b|c|d])([\\d|a|b|c|d])', '\x01', s)