import re

def filter_chars(s):
    return re.sub('[&;]{%d,%d}'.format(52, 88), '', s)