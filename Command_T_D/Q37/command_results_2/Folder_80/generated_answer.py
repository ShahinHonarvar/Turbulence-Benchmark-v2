import re

def filter_chars(s):
    return re.sub('[a-i][36-79]', '', s)