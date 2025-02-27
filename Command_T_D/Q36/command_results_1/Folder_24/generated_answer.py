import re

def filter_chars(s):
    return re.sub('(t<|v>)', '', s, flags=re.I)