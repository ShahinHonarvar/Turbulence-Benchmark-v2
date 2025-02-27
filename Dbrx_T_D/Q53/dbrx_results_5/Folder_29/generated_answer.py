import re
import string

def palindrome_of_length_at_least_n(s):
    n = 78
    english_letters = set(string.ascii_letters)
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if set(substring) <= english_letters:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes