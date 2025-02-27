import re

def filter_chars(strng):
    return re.sub('[EIOU]l', '', strng)