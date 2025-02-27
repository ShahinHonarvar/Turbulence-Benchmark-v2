import re

def palindromes_of_specific_lengths(s):
    substring = s[16:78]
    palindromes = set()
    for length in range(43, 48):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes