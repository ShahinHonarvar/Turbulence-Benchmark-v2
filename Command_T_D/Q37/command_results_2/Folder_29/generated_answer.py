import re

def filter_chars(s):
    return re.sub('[&v]', '', s, flags=re.I)