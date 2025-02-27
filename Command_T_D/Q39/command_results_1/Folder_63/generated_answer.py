import re

def return_n_greatest_chars(s):
    return sorted(re.findall('[A-Z]{%d}'.format(44), s), key=lambda x: ord(x))