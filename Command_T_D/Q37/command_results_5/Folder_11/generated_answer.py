import re

def filter_chars(s):
    return re.sub('([-o]?)[0-9]', '\x01', s)