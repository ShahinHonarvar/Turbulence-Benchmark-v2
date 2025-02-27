import re

def filter_chars(str1):
    return re.sub('[A-z][^sH]+', '', str1)