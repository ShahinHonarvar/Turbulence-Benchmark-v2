import re

def if_contains_anagrams(s):
    return bool(re.findall('\\A[a-z]{3}([a-z]{2,7})[a-z]{3}\\Z', s))