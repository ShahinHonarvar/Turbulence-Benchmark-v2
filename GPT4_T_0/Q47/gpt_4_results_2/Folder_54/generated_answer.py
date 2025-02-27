import re

def palindromes_of_specific_lengths(s):
    s = s[27:78]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 18, min(i + 20, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[A-Za-z]*$', substring):
                palindromes.add(substring.lower())
    return palindromes