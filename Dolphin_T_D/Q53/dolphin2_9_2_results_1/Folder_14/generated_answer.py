import re

def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 12):
        sub = s[i:i + 13]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes