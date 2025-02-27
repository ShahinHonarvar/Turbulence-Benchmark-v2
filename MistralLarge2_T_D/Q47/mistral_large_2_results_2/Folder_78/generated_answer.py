import re

def palindromes_of_specific_lengths(s):
    substring = s[15:73].lower()
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and re.match('^[A-Za-z]*$', candidate):
                palindromes.add(candidate)
    return palindromes