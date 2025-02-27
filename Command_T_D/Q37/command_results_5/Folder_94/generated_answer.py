import re

def filter_chars(s):
    return re.sub('[A-P]{%d,%d}'.format(51, 96), '', s)