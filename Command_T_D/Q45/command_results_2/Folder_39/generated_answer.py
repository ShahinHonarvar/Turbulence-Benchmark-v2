import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=([a-z]{2,})\x02)', s[2:-2]))