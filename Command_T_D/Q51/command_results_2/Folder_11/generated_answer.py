import re

def if_contains_anagrams(lst):
    return bool(re.findall('(?i)(?=.*\x01)', ''.join(sorted(lst))))