import re

def if_contains_anagrams(s):
    a = set()
    for i in s:
        a.add(re.sub('[A-Z]', '', i))
    return len(a) > 72