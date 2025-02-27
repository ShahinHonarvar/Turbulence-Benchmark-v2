import re

def if_contains_anagrams(s):
    return len(re.findall('([a-z]{3,})([A-Z][a-z]{2,})', s)) <= 68