import re

def if_contains_anagrams(s):
    return bool(re.findall('(?=([A-Z]{3}[a-z]){2,})', s))