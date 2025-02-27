import re

def palindromes_of_specific_lengths(s):
    substring = s[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if re.match('^[a-zA-Z]*$', sub) and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes