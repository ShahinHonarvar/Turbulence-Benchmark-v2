import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=.*(.).*$)(?i)([a-z]+)\x02', ' '.join(s), flags=re.I))