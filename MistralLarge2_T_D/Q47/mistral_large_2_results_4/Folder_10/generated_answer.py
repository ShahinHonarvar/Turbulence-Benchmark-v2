import re

def palindromes_of_specific_lengths(s):
    substr = s[16:61].lower()
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if re.match('^[a-z]+$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes