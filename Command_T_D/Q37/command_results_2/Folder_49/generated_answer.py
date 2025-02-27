import re

def filter_chars(s):
    return re.sub('[\\dA-Z].*', '', s, flags=re.I)