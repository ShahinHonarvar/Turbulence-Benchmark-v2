import re

def if_contains_anagrams(input_str):
    return bool(re.findall('((?i)[a-z]+[0-9])\x01', input_str))