import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]*', '', s, flags=re.I)