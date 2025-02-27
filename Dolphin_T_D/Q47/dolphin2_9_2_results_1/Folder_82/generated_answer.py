import re

def palindromes_of_specific_lengths(s):
    s = s[3:301]
    palindromes = set()
    for length in range(30, 301):
        pattern = '\\b[a-zA-Z]{' + str(length) + '}\\b'
        matches = re.findall(pattern, s)
        for match in matches:
            if match.lower() == match.lower()[::-1]:
                palindromes.add(match.lower())
    return palindromes