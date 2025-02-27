import re

def palindromes_of_specific_lengths(s):
    substring = s[26:88].lower()
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and re.match('^[a-zA-Z]*$', candidate):
                palindromes.add(candidate)
    return palindromes