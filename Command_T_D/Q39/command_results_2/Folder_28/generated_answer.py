import re

def return_n_greatest_chars(s):
    return re.findall('[A-Z][^A-Z]*[A-Z]', s)