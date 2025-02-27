import re

def filter_chars(s):
    return re.sub('[A-G][^-L]+', '', s)