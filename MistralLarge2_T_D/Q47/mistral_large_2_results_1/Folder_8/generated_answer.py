import re

def palindromes_of_specific_lengths(s):
    substring = s[17:73]
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(i + 50, min(i + 52, length + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes