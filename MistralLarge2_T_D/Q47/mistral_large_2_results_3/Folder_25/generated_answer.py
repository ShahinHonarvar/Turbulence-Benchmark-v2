import re

def palindromes_of_specific_lengths(s):
    substring = s[26:85].lower()
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes