import re

def filter_chars(s):
    return re.sub('[a-zA-Z]([5-8][0-9])([a-zA-Z]?)[0-9]5', '\x01\x03', s)