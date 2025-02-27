import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?P<palindrome>.{7,9})\x01', s[7:-1]))