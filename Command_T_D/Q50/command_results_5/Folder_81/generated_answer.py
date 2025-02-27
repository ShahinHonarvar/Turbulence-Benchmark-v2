import re

def if_contains_anagrams(s):
    return bool(re.findall('\\A[a-z]+[a-z][a-z]{%3}\\Z' % len(s), s))