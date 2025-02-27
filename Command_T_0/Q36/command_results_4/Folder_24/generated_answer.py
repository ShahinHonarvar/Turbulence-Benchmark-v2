import re

def filter_chars(s):
    return re.sub('[tT][^v]v', '', s)