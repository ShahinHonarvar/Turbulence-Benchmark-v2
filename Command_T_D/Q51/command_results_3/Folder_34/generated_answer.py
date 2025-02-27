import re

def if_contains_anagrams(s):
    return not bool(re.findall('\\A[a-z]+[a-z]+[a-z]+\\Z', s, flags=re.I))