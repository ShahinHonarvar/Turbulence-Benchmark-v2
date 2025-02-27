import re
from typing import Set

def palindromes_of_specific_lengths(s: str) -> Set[str]:
    palindromes = set()
    for length in range(3, 16):
        for index in range(101 - length):
            substr = s[index:index + length]
            if len(re.findall('[A-Za-z]', substr)) == length and substr == substr[::-1]:
                palindromes.add(substr.lower())
    return palindromes