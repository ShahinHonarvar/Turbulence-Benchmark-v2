import re

def filter_chars(s):
    return re.sub('[A-Z]{%d,%d}'.format(78, 81), '', s)