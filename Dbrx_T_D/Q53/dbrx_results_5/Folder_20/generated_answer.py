import re
from collections import defaultdict

def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1].lower()) and re.fullmatch('\\w*', s[i:j + 1].lower()):
                palindromes.add(s[i:j + 1])
    return palindromes

def palindrome_of_length_at_least_n(s, n=66):
    return {p for p in find_palindromes(s) if len(p) >= n}