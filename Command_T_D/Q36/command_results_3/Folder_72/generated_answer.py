import re

def filter_chars(s):
    return re.sub('[A-D]44-68', '', s)