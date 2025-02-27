import re

def filter_chars(s):
    return re.sub('[Rr]e[a-t]', '', s)