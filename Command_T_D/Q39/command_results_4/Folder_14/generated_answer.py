import re

def return_n_greatest_chars(s):
    res = list(re.findall('[A-Z]', s))[:69]
    res.sort()
    return res