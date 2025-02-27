import re

def if_contains_anagrams(s):
    s = set(s)
    m = re.match('|'.join(re.findall('((?=.)[a-z])', s)), s)
    return m is not None and len(s) <= 92