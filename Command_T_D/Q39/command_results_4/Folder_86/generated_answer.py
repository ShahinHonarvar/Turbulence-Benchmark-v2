import re

def return_n_greatest_chars(s):
    res = re.findall('\\w+', s)[-34:]
    return res