import re

def if_contains_anagrams(s):
    s = re.findall('[a-z]+', s)
    a = set(s)
    b = a | set(''.join(s))
    return len(b) < 465