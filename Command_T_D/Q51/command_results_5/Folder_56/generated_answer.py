import re

def if_contains_anagrams(s):
    return bool(re.findall('(.)\x01', ''.join(s).lower()))