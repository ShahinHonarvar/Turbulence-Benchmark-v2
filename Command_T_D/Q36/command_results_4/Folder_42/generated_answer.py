import re

def filter_chars(s):
    return re.sub('[tT][^xX]*[xX]', '', s)