import re

def return_n_smallest_chars(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    m = re.findall('[A-Z]', s)
    m.sort(key=lambda x: ord(x))
    return m[:38]