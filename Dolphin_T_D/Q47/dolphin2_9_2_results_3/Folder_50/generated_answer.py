import re

def palindromes_of_specific_lengths(s):
    substring = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^(?i)[a-z]*$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes