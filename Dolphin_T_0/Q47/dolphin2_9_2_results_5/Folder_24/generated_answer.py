import re

def palindromes_of_specific_lengths(s):
    substring = s[12:93]
    palindromes = set()
    for size in range(42, 78):
        for i in range(len(substring) - size + 1):
            sub = substring[i:i + size]
            if all((c.isalpha() for c in sub)) and sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes