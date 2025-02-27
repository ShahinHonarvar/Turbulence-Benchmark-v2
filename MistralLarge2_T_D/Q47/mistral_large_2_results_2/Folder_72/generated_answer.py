import re

def palindromes_of_specific_lengths(s):
    substring = s[26:91]
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes