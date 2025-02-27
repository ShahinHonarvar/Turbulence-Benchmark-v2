import re

def filter_chars(s):
    return re.sub('[A-Z][2-s]', '', s)