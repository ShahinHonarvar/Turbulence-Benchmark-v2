import re

def palindromes_of_specific_lengths(s):
    substring = s[28:95]
    palindromes = set()
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[a-zA-Z]*$', candidate):
                if candidate.lower() == candidate.lower()[::-1]:
                    palindromes.add(candidate)
    return palindromes