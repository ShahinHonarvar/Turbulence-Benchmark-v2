import re

def if_contains_anagrams(s):
    return bool(re.findall('\\A[a-z]{3}]+\\Z', ''.join(s), flags=re.I))