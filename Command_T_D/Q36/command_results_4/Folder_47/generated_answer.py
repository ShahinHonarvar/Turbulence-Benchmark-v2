import re

def filter_chars(s):
    return re.sub('[G-n]{%d,%d}'.format(45, 57), '', s)