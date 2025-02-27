import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}'.format(86, 92), '', s)