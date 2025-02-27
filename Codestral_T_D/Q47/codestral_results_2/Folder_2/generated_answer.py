import re

def palindromes_of_specific_lengths(s):
    s = s[10:60]
    palindromes = set()
    for l in range(18, 37):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes