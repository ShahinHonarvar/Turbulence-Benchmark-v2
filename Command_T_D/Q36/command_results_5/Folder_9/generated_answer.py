import re

def filter_chars(str):
    return re.sub('[A-Q][^A-Q]*', '', str)