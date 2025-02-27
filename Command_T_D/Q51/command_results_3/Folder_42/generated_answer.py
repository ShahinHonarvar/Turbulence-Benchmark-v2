import re

def if_contains_anagrams(s):
    s = [x.lower() for x in s]
    return len(re.findall('(?=([a-z]+[a-z]+[a-z]+))', '|'.join(s))) <= 38