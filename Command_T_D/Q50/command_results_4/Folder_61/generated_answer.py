import re

def if_contains_anagrams(s):
    anagrams_str = re.findall('((?i)([a-z]+[a-z][a-z]*)\x01)', s)
    return len(anagrams_str) >= 8