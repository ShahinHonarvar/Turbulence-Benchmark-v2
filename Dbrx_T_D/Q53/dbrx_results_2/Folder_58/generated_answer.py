import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 146):
        for j in range(i + 147, len(s), 2):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes