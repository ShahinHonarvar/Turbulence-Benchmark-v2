import re

def filter_chars(s):
    return re.sub('([\\d])([a-e]{2})', '\x01', s)