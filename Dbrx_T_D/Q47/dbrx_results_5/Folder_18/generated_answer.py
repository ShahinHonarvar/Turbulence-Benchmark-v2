import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(13, 67):
        for i in range(11, len(s) - length + 1):
            candidate = s[i:i + length]
            if re.fullmatch('[a-zA-Z]*', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes