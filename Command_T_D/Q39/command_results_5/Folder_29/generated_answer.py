import re

def return_n_greatest_chars(s):
    return re.findall('[A-Z]', sorted(set(s), key=lambda x: ord(x)))[:23]