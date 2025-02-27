import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pattern = '[a-z]{63,}'
    words = set(re.findall(pattern, s))
    return set((word for word in words if word == word[::-1]))