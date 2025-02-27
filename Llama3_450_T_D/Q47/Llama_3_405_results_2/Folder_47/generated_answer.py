import re

def palindromes_of_specific_lengths(s):
    s = s[39:95].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 14, min(i + 53, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                palindromes.add(substr)
    return palindromes