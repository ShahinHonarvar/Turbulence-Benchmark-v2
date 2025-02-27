import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]44[^A-Z]E', '', s)