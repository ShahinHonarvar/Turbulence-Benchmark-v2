import re

def if_contains_anagrams(s):
    return len(re.findall('(?i)(?=([a-z]+\x01)+[a-z]+\x02)', s)) <= 49