import re
from string import ascii_letters

def palindrome_of_length_at_least_n(n, text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - n + 1):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and all((char in ascii_letters for char in substring)):
                palindromes.add(substring)
    return palindromes