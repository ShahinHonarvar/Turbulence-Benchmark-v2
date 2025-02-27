import re

def filter_chars(str1):
    return re.sub('[a-z]', '', str1)