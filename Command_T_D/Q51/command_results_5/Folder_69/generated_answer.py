import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=.*[aeiou])(?=.*[aeiou])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[-])(?=.*[.]).*', s))