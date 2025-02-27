import re

def palindromes_of_specific_lengths(s):
    substr = s[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if re.match('^[a-zA-Z]+$', substring) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes