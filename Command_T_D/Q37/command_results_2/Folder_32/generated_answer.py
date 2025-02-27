import re

def filter_chars(str):
    return re.sub('[A-Z][a-z]{%d,%d}'.format(23, 89), '', str)