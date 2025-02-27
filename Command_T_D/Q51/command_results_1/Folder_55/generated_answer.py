import re

def if_contains_anagrams(s):
    return bool(re.findall('((?i)(?=.*[a-z]))((?i)(?=.*[a-z]))', s))