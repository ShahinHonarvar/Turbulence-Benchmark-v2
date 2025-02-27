import re

def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 16):
        for j in range(17, len(s) - i + 1):
            substring = s[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes