import re

def filter_chars(s):
    return re.sub('(.*?[a-z])(.*?)', '\x01\x02', s)