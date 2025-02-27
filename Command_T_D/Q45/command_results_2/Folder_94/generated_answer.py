import re

def palindromes_between_indices(s):
    if not s:
        return set()
    else:
        return set(re.findall('(?=.)(.)\x01', s[3:-4].lower()))