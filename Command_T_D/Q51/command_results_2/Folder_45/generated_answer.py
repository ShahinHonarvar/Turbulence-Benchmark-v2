import re

def if_contains_anagrams(s):
    return bool(re.findall('\\A(.*?[A-Z])(.*?[A-Z])(.*?[A-Z])(.*?[A-Z])\\Z', s, flags=re.I))