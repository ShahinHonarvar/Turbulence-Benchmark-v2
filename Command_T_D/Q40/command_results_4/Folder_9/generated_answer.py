import re

def return_n_smallest_chars(s):
    res = re.findall('[A-Z]', s)
    return res[:20]