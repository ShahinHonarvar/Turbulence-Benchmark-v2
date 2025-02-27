import re

def if_contains_anagrams(s):
    return not re.search('(.)\x01+', s, flags=re.I) and len(set(s)) == len(s)