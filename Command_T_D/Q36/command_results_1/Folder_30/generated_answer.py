import re

def filter_chars(string):
    return re.sub('(\\d+)([a-i])', '\x01', string)