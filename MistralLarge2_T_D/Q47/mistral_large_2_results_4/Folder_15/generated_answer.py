import re

def palindromes_of_specific_lengths(s):
    substring = s[0:7].lower()
    palindromes = set()
    for length in range(3, 7):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[a-z]+$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes