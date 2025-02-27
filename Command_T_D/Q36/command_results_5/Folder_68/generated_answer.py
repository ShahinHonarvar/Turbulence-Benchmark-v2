import re

def filter_chars(s):
    return re.sub('([1-9])', '\x01', s)