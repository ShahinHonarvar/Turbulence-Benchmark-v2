import re

def palindromes_of_specific_lengths(s):
    substring = s[22:96].lower()
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[a-z]*$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes