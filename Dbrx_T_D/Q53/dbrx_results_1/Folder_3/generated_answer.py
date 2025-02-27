import re
from collections import defaultdict

def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(s):
    s = re.sub('\\W+', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes

def palindrome_of_length_at_least_n(s, n=59):
    palindromes = find_palindromes(s)
    return {p for p in palindromes if len(p) >= n}