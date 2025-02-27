import re

def filter_chars(str):
    return re.sub('[a-z]{%d,%d}'.format(41, 86), '', str)