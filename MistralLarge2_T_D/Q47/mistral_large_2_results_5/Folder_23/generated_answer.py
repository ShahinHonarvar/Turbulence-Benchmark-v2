import re

def palindromes_of_specific_lengths(s):
    substr = s[23:95].lower()
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate == candidate[::-1] and re.match('^[a-zA-Z]+$', candidate):
                palindromes.add(candidate)
    return palindromes