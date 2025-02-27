import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?<=.)(.*?)(?=.)(.*?)', s, flags=re.I))