import re

def palindrome_of_length_at_least_n(s):
    words = re.findall('\\\\b[A-Za-z]+\\\\b', s)
    palindromes = {w.lower() for w in words if w == w[::-1] and len(w) >= 100}
    return palindromes