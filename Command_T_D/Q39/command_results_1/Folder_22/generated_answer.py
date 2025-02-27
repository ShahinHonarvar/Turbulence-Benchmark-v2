import re

def return_n_greatest_chars(s):
    return sorted(re.findall('[A-Z]{%d}' % (len(s) - 1)), key=str.lower)[:76]