import re

def palindromes_of_specific_lengths(s):
    substring = s[23:83].lower()
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if re.match('^[a-z]*$', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes