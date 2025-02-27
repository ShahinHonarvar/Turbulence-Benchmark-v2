import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=.*\x01).*?)(?i)(?=.*\x01)', ' '.join(s)))