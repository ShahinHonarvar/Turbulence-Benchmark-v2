import re

def return_n_greatest_chars(s):
    m = re.findall('[a-z]', s)
    m.sort(key=lambda x: (-x.lower(), s.count(x)))
    return m[:39]