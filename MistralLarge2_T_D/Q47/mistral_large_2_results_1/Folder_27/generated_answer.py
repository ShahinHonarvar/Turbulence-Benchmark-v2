import re

def palindromes_of_specific_lengths(s):
    substring = s[13:100]
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[A-Za-z]*$', candidate) and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes