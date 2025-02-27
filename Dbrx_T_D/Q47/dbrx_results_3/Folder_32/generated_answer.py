import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(16, 78):
        for length in range(43, 48):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and re.match('[a-zA-Z]*$', substring):
                palindromes.add(substring)
    return palindromes