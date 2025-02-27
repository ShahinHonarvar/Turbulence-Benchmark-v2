import re

def palindromes_of_specific_lengths(string):
    substring = string[:7]
    palindromes = set()
    for length in range(3, 7):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[A-Za-z]*$', candidate) and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes