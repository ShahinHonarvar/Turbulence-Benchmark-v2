import re

def palindromes_of_specific_lengths(s):
    substring = s[10:60]
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(i + 18, min(i + 37, length + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes