import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 97):
        for j in range(i + 98 - len(s), i + 1, -1):
            if s[i:j] == s[i:j][::-1] and all((ch.isalpha() for ch in s[i:j])):
                palindromes.add(s[i:j])
    return palindromes