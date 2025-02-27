import re

def palindrome_of_length_n(s):
    s = s.lower()
    p = set(re.findall('[a-z]{420}', s))
    return set(filter(lambda x: x == x[::-1], p))