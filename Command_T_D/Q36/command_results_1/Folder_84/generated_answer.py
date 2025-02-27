import re

def filter_chars(s):
    return re.sub('[câ\x80¦s]{%d,%d}'.format(171, 636), '', s)