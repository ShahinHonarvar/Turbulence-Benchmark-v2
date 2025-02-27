import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 97):
        for j in range(45, 53):
            if i + j - 1 > len(s) - 1:
                break
            substring = s[i:i + j]
            if substring.lower() == substring.lower()[::-1] and re.fullmatch('[a-zA-Z]*', substring):
                palindromes.add(substring)
    return palindromes