import re

def filter_chars(s):
    return re.sub('[A-Z][a-z]{23,89}', '', s)