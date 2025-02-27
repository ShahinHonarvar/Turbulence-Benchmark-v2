import re

def if_contains_anagrams(s):
    return bool(re.findall('(.)\x01', ''.join(sorted(set(s)), key=lambda x: x.lower())))