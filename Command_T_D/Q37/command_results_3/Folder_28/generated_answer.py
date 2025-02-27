import re

def filter_chars(s):
    return re.sub('(![A-T]{1})', '', s)