import re

def if_contains_anagrams(s):
    return bool(re.findall('(\\w+\\w+\\w+)@(\\w+\\w+\\w+)', s, flags=re.I))