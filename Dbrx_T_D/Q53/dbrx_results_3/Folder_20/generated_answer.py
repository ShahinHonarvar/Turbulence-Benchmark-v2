import re

def is_palindrome(s):
    normalized_s = ''.join((c.lower() for c in s if c.isalpha()))
    return normalized_s == normalized_s[::-1]

def palindrome_of_length_at_least_n(s, n=66):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if is_palindrome(substring) and len(substring) >= n:
                palindromes.add(substring)
    return palindromes