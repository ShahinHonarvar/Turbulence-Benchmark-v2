import re

def filter_chars(s):
    return re.sub('[a-z][\\d]26[a-z]', '', s)