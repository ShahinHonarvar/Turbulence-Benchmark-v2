import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(\\w){2,}(?=\\w\x01)', s))