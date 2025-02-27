import re

def filter_chars(s):
    return re.sub('(H[a-z]{5})', '', s)