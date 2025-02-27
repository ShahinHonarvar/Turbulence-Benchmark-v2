import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 42, len(s) + 1):
            substr = s[i:j]
            if re.match('^[a-z]+$', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes