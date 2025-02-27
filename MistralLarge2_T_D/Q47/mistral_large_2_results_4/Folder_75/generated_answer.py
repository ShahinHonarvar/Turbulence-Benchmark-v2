import re

def palindromes_of_specific_lengths(s):
    substring = s[31:75].lower()
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                palindromes.add(substr)
    return palindromes