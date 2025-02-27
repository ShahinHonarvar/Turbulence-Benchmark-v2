import re

def palindromes_of_specific_lengths(s):
    substring = s[11:88].lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                palindromes.add(substr)
    return palindromes