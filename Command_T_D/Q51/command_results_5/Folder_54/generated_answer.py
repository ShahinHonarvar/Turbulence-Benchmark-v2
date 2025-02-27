import re

def if_contains_anagrams(s):
    return len(s) * len(s) <= 39 and len(set(s)) <= 39 and (len(re.findall('(?i)(?=([^aieou])\x01)', ' '.join(s))) <= 39)