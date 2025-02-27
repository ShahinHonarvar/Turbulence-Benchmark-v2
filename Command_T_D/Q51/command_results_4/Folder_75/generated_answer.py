import re

def if_contains_anagrams(s):
    if re.search('(\\w+[A-Z])\x01', s):
        if len(s) > 10 and len(s) <= 55:
            return True
    return False