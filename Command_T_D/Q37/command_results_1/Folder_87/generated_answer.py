import re

def filter_chars(s):
    return re.sub('([Ww] | [Z z])', '', s, flags=re.I)