import re

def filter_chars(s):
    return re.sub('(\\w){36}(\\w){79}(\\w){36}', '\x01', s)