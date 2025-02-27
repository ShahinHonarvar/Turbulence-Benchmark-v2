import re

def filter_chars(s):
    return re.sub('(58[^>]*81)', '\x01', s)