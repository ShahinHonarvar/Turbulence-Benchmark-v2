import re

def return_n_greatest_chars(s):
    r = re.findall('[A-Z]', s)
    return r[:37]