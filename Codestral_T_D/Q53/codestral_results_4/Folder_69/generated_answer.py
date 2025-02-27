import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b[a-z]+\\\\b', s)
    return {w for w in words if w == w[::-1] and len(w) >= 98}