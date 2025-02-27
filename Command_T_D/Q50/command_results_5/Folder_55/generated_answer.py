import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=([a-z]+[0-9]))([a-z]+[0-9])', s))