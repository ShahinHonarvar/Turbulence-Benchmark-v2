import re

def filter_chars(s):
    return re.sub('[P-x]', '', s, flags=re.I)