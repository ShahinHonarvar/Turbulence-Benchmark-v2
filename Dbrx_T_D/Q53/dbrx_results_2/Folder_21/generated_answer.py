import re

def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 111):
        for j in range(i + 112, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and re.fullmatch('[a-zA-Z]+', substring):
                palindromes.add(substring)
    return palindromes