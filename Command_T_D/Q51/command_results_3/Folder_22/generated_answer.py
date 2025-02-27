import re

def if_contains_anagrams(input_str):
    for s in input_str:
        if re.search('([A-Z])\x01+', s.lower()):
            return True
    return False