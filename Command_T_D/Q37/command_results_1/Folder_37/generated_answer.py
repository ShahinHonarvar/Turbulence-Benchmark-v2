import re

def filter_chars(str1):
    return re.sub('[O-^]', '', str1)