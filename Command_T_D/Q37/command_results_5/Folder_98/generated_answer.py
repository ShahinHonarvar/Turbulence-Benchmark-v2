import re

def filter_chars(s):
    return re.sub('[Rr]t', '', s)