import re

def if_contains_anagrams(s):
    return len(set(re.findall('(?i)(?:[a-z]+){2,}'.format(s), s))) <= 36