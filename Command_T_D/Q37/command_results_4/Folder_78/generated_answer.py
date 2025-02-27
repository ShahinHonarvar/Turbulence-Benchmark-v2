import re

def filter_chars(s):
    return re.sub('[8e]{%d,%d}[^8e]{%d,%d}'.format(75, 99), '', s)