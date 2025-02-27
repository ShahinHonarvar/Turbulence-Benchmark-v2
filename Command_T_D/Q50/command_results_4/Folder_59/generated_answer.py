import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(\\w){3}(?i)\x01', s))