import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(64, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                palindromes.add(substr)
    return palindromes