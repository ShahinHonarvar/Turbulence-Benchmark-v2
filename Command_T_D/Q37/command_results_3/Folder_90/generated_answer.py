import re

def filter_chars(str):
    return re.sub('((?:[A-Z]\\d)\\d)\\d', '\x01', str)