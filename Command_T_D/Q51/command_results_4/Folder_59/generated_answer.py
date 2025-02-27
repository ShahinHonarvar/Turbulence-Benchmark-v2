import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=.*[A-Z])([A-Z][^A-Z]*)(?=.*[A-Z])', ' '.join(s)))