import re

def return_n_greatest_chars(s):
    a = re.findall('[A-Z]', s)
    return a[:5]