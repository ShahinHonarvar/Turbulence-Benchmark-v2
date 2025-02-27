import re

def palindromes_of_specific_lengths(s):
    substring = s[130:296].lower()
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and re.match('^[a-zA-Z]*$', candidate):
                palindromes.add(candidate)
    return palindromes