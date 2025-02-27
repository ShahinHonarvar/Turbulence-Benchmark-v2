import re

def filter_chars(str):
    return re.sub('[EIOU]', '', str, flags=re.I)