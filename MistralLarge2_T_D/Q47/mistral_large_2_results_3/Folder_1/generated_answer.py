import re

def palindromes_of_specific_lengths(s):
    substring = s[15:90]
    palindromes = set()
    n = len(substring)
    for length in range(40, 73):
        for i in range(n - length + 1):
            candidate = substring[i:i + length]
            if re.fullmatch('[a-zA-Z]*', candidate) and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes