import re

def filter_chars(s):
    return re.sub('[6-9][A-Z]', '', s)