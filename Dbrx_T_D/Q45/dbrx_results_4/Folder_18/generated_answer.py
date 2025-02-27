import re
import string

def palindromes_between_indices(s: str) -> set:
    english_letters = set(string.ascii_lowercase + string.ascii_uppercase)
    s = s.lower()
    palindromes = set()
    for i in range(1, min(6, len(s)) + 1):
        for j in range(i, min(6 + i, len(s)) + 1):
            substring = s[j - 1:j + i]
            if set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes