import re

def palindromes_between_indices(s):
    for i in range(1, min(len(s), 10)):
        s += s[:i]
    if s[0] == s[len(s) // 2]:
        s = s[1:-1]
    return set(re.findall('([A-Z])\x01+', s.lower()))