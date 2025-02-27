import re

def filter_chars(s):
    return re.sub('[A-Z][^A-Z]F[A-Z][^A-Z]h', '', s)