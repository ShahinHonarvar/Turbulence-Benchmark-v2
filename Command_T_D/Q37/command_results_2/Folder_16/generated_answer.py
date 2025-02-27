import re

def filter_chars(s):
    return re.sub('[D-Y]', '', s, flags=re.I)