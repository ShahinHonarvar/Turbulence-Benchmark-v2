import re
from collections import defaultdict

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(30, 301):
        for start in range(3, 301 - length + 1):
            end = start + length - 1
            if s[start:end + 1] == s[start:end + 1][::-1]:
                palindromes.add(s[start:end + 1])
    return palindromes