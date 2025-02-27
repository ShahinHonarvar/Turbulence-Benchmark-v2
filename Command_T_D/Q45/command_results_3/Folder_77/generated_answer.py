import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=([^aieou]))(.)(.)(.)(.)(.)', s[4:-2]))