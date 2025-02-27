import re

def filter_chars(s):
    return re.sub('[A-Z][a-z]11[A-Z][a-z]32[A-Z][a-z]![A-Z][a-z]@', '', s)