import re

def filter_chars(s):
    return re.sub('[a-z][\\d]25[a-z][\\d]97[a-z][\\d]', '', s)