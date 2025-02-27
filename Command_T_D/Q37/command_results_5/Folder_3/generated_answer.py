import re

def filter_chars(s):
    return re.sub('([A-Z])([37-56])([A-Z]_)?', '\x01', s)