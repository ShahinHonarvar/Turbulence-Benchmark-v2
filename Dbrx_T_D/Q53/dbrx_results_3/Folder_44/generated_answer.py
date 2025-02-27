import re
import string

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=89):
    s = s.lower()
    s = ''.join((c for c in s if c in string.ascii_letters))
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes