import re

def palindromes_between_indices(s):
    for i in range(3, 5):
        s += s[i:i + i]
    return set(re.findall('((?i)[a-z]+)\x01', s))