import re

def if_contains_anagrams(s):
    return bool(re.findall('(\\A[A-Z]+[a-z]+[A-Z]+)+', ''.join(s), flags=re.I))