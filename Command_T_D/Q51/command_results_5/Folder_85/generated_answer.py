import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=.*[aeiou])(?=.*[aeiou])(?=.*[a-z])(?=.*[a-z])\x01\x02\x03', s))