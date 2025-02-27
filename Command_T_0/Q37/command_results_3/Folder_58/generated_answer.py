import re

def filter_chars(s):
    return re.sub('[0-9][A-Z][a-z]', '', s)