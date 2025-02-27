import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(\\w)(?=\\w\x01)', s))