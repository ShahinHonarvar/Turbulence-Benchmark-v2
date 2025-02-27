import re
from collections import defaultdict

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(30, 301):
        for i in range(3, len(s) - length + 1):
            substring = s[i:i + length]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes