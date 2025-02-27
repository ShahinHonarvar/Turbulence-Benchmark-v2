import re

def filter_chars(s):
    return re.sub('[A-E][^H-e]', '', s)