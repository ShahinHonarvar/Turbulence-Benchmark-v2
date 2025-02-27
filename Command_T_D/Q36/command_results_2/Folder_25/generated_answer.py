import re

def filter_chars(s):
    return re.sub('[A-g]+', '', s)