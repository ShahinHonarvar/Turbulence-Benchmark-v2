import re

def filter_chars(s):
    return re.sub('(>X<)', '', s, flags=re.I)