import re

def filter_chars(s):
    return re.sub('[Oo][A-d]', '', s)