import re

def filter_chars(str):
    return re.sub('[A-Z]{%d,%d}'.format(39, 87), '', str)