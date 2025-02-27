import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(\\S{3})\x01', ''.join(s)))