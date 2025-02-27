import re

def filter_chars(s):
    return re.sub('[+\\d]', '', s, flags=re.I)