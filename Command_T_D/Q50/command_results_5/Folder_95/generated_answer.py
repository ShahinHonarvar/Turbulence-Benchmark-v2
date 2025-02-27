import re

def if_contains_anagrams(lst):
    return bool(re.findall('(?i)(?=.*\x01)', *sorted(lst), key=lambda x: (len(x), len(set(x))))).count(True) >= 93