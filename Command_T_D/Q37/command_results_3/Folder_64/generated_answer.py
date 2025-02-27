import re

def filter_chars(str):
    return re.sub('[A-Z]{%d,%d}'.format(1, 7), '', str)