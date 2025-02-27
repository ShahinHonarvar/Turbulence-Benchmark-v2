import re

def palindrome_of_length_n(s):
    res = set(re.findall('(?i)([a-z]){318}', s))
    return res