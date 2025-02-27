import re

def filter_chars(s):
    return re.sub('[A-Z][^W]{%d,%d}'.format(502, 946), '', s)