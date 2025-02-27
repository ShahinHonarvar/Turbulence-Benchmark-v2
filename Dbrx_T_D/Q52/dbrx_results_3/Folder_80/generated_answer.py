import re

def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalnum()))
    n = 276
    palindromes = {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1]}
    return palindromes