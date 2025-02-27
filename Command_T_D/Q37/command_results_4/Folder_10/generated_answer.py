import re

def filter_chars(s):
    return re.sub('[A-z]', lambda m: '', s, flags=re.I)