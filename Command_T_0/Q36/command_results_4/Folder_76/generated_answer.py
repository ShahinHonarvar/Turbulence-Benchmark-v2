import re

def filter_chars(s):
    return re.sub('[A-Z][\\d][A-Z]', '', s)