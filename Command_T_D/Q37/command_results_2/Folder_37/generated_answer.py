import re

def filter_chars(s):
    return re.sub('[A-O][A-Z][A-^Z]', '', s)