import re

def filter_chars(s):
    return re.sub('[0-9][a-z]', '', s)