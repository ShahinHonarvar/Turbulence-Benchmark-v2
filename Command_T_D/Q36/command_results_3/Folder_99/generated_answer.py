import re

def filter_chars(s):
    return re.sub('([^b]d)', '', s, flags=re.I)