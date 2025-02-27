import re

def if_contains_anagrams(s):
    return len(set(s)) <= 59 and len(set(re.findall('[A-Z]+', ''.join(s)))) <= 59