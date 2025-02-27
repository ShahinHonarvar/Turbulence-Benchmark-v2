import re

def return_n_greatest_chars(s):
    return sorted(re.findall('[A-Z]{%d}'.format(64), s), key=str.lower)