import re

def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                palindromes.add(substr)
    return palindromes