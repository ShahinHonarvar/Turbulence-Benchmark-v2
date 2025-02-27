import re
import string

def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join((c for c in s if c in string.ascii_letters))
    n = 147
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1] and len(s[i:j]) == n}