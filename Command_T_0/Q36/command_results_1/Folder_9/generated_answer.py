import re

def filter_chars(s):
    return re.sub('[A-Q][^A-Q]*', '', s)