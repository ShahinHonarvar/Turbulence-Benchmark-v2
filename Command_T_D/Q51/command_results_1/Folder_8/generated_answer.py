import re

def if_contains_anagrams(s):
    return bool(re.findall('\\A[a-z]+\\Z', s, flags=re.I))