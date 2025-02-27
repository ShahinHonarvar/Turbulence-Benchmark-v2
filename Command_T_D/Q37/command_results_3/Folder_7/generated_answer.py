import re

def filter_chars(s):
    return re.sub('(?<=>)[^_]{%d,%d}(?=_)' % (521, 722), '', s)