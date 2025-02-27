import re

def filter_chars(s):
    return re.sub('[+\\-]{%d,%d}'.format(515, 538), '', s)