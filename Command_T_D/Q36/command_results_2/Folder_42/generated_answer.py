import re

def filter_chars(string):
    return re.sub('(\\w+)[A-Z]', '\x01', string)