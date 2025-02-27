import re

def filter_chars(str1):
    return re.sub('[A-Z][^A-Z]', '', str1)