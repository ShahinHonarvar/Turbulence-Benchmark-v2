import re

def palindromes_between_indices(s):
    res = set(re.findall('(?i)(?P<s>.)\x01(?P<t>.){2}(?P<s>.){2}(?P=t)\x01(?P=s)', s[2:-6:-2]))
    return res