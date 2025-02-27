import re

def palindrome_of_length_n(s):
    s = s.lower()
    pattern = '[a-zA-Z]{113}'
    matches = set(re.findall(pattern, s))
    return set(filter(lambda x: x == x[::-1], matches))