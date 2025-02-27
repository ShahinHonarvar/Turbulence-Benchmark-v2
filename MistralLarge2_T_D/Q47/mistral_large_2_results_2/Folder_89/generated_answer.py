import re

def palindromes_of_specific_lengths(s):
    substring = s[18:89].lower()
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and re.fullmatch('[a-z]+', candidate):
                palindromes.add(candidate)
    return palindromes