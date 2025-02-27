import re

def filter_chars(s):
    return re.sub('[A-W][^x]+', '', s)