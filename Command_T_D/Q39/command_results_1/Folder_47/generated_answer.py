import re

def return_n_greatest_chars(s):
    return re.findall('[a-z]', sorted(s)[-21:])