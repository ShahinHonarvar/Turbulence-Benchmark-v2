import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}'.format(44, 68), '', s)