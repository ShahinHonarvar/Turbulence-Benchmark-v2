import re

def filter_chars(s):
    return re.sub('[f|]{%d,%d}'.format(41, 79), '', s)