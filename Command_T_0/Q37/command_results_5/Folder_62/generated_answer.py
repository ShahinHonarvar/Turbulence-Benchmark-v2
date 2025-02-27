import re

def filter_chars(s):
    return re.sub('[I-K]', '', s)