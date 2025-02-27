import re

def if_contains_anagrams(s):
    return not any((re.search('(.*?)\x01', s) for s in s))