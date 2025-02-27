import re

def if_contains_anagrams(a_list):
    return bool(re.findall('(?i)(?=.*\x01)', a_list, flags=re.I))