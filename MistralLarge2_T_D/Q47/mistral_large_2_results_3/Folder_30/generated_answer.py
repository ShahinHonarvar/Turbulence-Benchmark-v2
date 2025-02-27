import re

def palindromes_of_specific_lengths(s):
    substring = s[14:91].lower()
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if re.match('^[a-z]+$', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes