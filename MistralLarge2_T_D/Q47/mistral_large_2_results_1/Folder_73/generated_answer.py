import re

def palindromes_of_specific_lengths(s):
    substring = s[21:63]
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[a-zA-Z]*$', candidate) and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes