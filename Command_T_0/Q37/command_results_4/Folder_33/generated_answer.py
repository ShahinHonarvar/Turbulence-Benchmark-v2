import re

def filter_chars(s):
    return re.sub('[K-m]', '', s, flags=re.I)