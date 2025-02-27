import re
from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s.lower()
    n = 33
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n - 1, i - 1, -2):
            if s[i:j + 1] == s[i:j + 1][::-1] and all((c in english_letters for c in s[i:j + 1])):
                palindromes.add(s[i:j + 1])
    return palindromes