import re

def filter_chars(s):
    return re.sub('[,;]{%d,%d}'.format(259, 502), '', s)