import re

def return_n_greatest_chars(s):
    res = re.findall('[A-Z]+', s)[:80]
    return ''.join(sorted(res))