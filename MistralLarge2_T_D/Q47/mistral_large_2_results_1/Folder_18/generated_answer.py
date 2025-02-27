import re

def palindromes_of_specific_lengths(s):
    substring = s[11:84]
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if re.match('^[A-Za-z]*$', sub) and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes