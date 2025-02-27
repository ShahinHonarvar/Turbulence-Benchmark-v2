import re

def filter_chars(s):
    return re.sub('[a-z]{12,77}', '', s)