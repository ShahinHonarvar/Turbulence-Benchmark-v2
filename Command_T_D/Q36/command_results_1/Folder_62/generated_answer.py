import re

def filter_chars(s):
    return re.sub('[A-Za-z]', lambda m: m.group(), s)