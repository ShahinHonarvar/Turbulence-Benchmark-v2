from typing import Set

def palindrome_of_length_n(s: str) -> Set[str]:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for j in range(i + 51, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes