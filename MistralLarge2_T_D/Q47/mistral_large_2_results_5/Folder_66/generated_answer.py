import re

def palindromes_of_specific_lengths(s):
    substring = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes