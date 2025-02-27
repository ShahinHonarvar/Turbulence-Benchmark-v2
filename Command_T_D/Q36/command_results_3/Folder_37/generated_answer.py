import re

def filter_chars(s):
    return re.sub('[A-Z][0-5]', '', s)