import re

def filter_chars(s):
    return re.sub('[!x]', '', s, flags=re.I)