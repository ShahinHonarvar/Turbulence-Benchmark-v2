import re

def filter_chars(s):
    return re.sub('[a-d]11', 'g', s)