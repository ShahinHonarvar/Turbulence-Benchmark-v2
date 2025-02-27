import re

def filter_chars(s):
    return re.sub('[7-k]', '', s)