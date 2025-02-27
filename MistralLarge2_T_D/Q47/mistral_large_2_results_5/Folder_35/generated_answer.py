import re

def palindromes_of_specific_lengths(s):
    substring = s[34:91].lower()
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and re.match('^[a-z]+$', candidate):
                palindromes.add(candidate)
    return palindromes