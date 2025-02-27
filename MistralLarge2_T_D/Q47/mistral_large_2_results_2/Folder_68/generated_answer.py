import re

def palindromes_of_specific_lengths(s):
    substring = s[:51].lower()
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[a-z]+$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes