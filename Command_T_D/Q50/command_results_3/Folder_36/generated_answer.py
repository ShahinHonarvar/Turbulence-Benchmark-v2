import re

def if_contains_anagrams(strs):
    return bool(re.findall('(?i)(?=.*\x01)', *strs))