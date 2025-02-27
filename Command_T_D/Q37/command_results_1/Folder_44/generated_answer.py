import re

def filter_chars(s):
    return re.sub('(([+\\d])\\d{3})', '\x01', s)