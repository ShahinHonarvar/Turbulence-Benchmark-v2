import re

def if_contains_anagrams(s):
    return bool(re.findall('((?=.*[A-Z])[A-Z]+)', s))