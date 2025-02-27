import re

def filter_chars(s):
    return re.sub('([P-x]{12,25})', '', s)