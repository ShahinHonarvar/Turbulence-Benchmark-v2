import re

def if_contains_anagrams(s):
    return len(re.findall('\\A[a-z]+\\Z', s)) <= 407