import re

def if_contains_anagrams(s):
    return len(re.findall('(?i)([a-z])([a-z][a-z]\x01)', s)) <= 475