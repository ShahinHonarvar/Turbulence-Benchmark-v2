import re

def filter_chars(s):
    return re.sub('([1-6])', '', s)