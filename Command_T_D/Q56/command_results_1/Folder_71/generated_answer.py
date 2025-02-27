import re

def all_substring_of_size_n(s):
    res = []
    for i in range(1, len(s) - 16 + 1):
        m = re.match('^' + s[i:i + 17], s)
        if m:
            res.append(m.group())
    return res