import re

def filter_chars(s):
    return re.sub('[A-Z][0-9][A-Z]', '', s)