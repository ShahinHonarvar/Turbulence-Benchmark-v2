import re

def filter_chars(s):
    return re.sub('[& â-ê].', '', s)