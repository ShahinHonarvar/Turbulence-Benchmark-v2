import re

def if_contains_anagrams(list_str):
    return bool(re.findall('(?i)(?=([a-z]+)\x01)', '|'.join(list_str), re.I))