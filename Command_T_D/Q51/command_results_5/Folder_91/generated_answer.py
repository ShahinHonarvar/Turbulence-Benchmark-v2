import re

def if_contains_anagrams(s):
    return len(set(s)) <= 88 and all((x.lower() != y.lower() for x, y in zip(s, s))) and (len(s) > 2) and all((re.match('(?=([a-z]))\x01+$', x.lower()) for x in s))