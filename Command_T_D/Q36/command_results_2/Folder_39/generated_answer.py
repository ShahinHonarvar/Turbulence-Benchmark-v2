import re

def filter_chars(string):
    return re.sub('[A-E]{%d,%d}'.format(43, 59), '', string)