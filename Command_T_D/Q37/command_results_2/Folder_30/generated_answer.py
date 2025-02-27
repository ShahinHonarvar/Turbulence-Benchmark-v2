import re

def filter_chars(s):
    return re.sub('(\\d{5})', '', s)