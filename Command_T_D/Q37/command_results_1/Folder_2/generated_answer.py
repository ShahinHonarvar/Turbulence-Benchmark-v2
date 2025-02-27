import re

def filter_chars(s):
    return re.sub('[\\d,A-Z][\\d,A-Z]', '', s)