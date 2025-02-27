import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=.*[aeiou])(.*?[aeiou])', ''.join(s), flags=re.I))