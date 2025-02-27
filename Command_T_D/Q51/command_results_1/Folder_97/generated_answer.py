import re

def if_contains_anagrams(input_str):
    return bool(re.findall('(?i)(?<=.)(?!\x01)[a-z]+\x01', input_str, flags=re.I))