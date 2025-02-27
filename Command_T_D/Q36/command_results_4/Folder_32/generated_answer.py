import re

def filter_chars(s):
    return re.sub('(?i)[a-z0-9](40,63)s', '', s)