import re

def filter_chars(s):
    return re.sub('[\\d]{1,2}|\\w|/|,|&|_', '', s, flags=re.I)