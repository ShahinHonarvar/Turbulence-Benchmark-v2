import re

def palindrome_of_length_n(s):
    s = s.lower()
    pattern = '[a-z]{222,222}\\\\b'
    matches = set(re.findall(pattern, s))
    return matches