import re

def if_contains_anagrams(s):
    return len(re.findall('(?i)(?=([a-z]+[A-Z][a-z])))', s)) <= 98