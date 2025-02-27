import re

def filter_chars(s):
    return re.sub('(([1-8]?)[0-9])', '\x01', s, flags=re.I)