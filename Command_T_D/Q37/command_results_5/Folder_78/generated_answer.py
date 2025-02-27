import re

def filter_chars(strng):
    return re.sub('[8e]{75,99}', '', strng)