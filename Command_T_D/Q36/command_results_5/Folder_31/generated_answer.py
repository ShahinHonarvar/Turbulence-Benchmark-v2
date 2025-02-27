import re

def filter_chars(s):
    return re.sub('[A-K]{%14,%75}', '', s)