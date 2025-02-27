import re

def filter_chars(s):
    return re.sub('([a-z]:[a-z]r)', '', s)