import re
import string

def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    english_letters = set(string.ascii_letters)
    palindromes = set()
    for i in range(len(s) - 75):
        substring = s[i:i + 76]
        if substring.isalpha() and set(substring) <= english_letters:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes