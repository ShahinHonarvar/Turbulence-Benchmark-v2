import re

def is_palindrome(s):
    s = ''.join((ch.lower() for ch in s if ch.isalpha()))
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=78):
    return {pal for pal in {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1)} if is_palindrome(pal)}