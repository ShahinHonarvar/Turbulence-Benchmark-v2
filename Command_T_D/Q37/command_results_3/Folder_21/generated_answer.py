import re

def filter_chars(str1):
    str1 = str(re.sub('[Qh]', '', str1))
    return str1