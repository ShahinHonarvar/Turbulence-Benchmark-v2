import re

def if_contains_anagrams(s):
    return not re.findall('((?i)[a-z]{3})\x01', s)