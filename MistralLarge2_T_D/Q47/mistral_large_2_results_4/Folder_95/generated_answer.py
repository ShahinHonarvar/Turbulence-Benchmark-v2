import re

def palindromes_of_specific_lengths(s):
    substring = s[12:57].lower()
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[a-zA-Z]*$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes