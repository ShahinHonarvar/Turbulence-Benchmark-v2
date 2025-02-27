import re
from collections import defaultdict

def palindromes_of_specific_lengths(s: str) -> set:
    s = s[3:301]
    palindromes = set()
    s_lower = s.lower()
    for length in range(30, 301):
        for i in range(len(s) - length + 1):
            substring = s_lower[i:i + length]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes