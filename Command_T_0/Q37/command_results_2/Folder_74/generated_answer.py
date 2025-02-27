import re

def filter_chars(s):
    return re.sub('[f-o]{%d,%d}'.format(19, 32), '', s)