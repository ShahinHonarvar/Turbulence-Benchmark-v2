import re

def filter_chars(s):
    return re.sub('(?i)[5-9_]{2}(?=[5-9_])', '', s)