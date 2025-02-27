import re

def filter_chars(s):
    return re.sub('[A-F]{%d,%d}'.format(154, 222), '', s)