import re

def filter_chars(str1):
    return re.sub('[a-z];[a-z]g', '', str1)