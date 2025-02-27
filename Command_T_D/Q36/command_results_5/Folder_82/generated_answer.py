import re

def filter_chars(s):
    return re.sub('(?i)(?:e|f|g|h|i|j)', '', s)