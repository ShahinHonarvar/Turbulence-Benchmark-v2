import re

def filter_chars(str):
    return re.sub('[A-f]{%d,%d}'.format(154, 222), '', str)