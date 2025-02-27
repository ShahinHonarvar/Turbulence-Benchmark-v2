import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]m[^A-Z]w[^A-Z]A-Z', '', s)