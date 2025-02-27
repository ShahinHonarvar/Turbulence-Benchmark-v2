import re

def if_contains_anagrams(s):
    return sum((1 for x in s if len(x) > 2 and len(set(x)) == 26 and (len(re.findall('(?i)(?=([^aieou]))\x01', x)) <= 77)))