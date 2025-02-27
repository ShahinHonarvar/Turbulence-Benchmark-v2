import string
import re

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    english_letters_in_range = ''.join((c for c in s[1:8] if c in english_letters))
    english_letters_in_range = english_letters_in_range.upper()
    palindromes = set()
    for i in range(5, len(english_letters_in_range) + 1):
        for j in range(len(english_letters_in_range) - i + 1):
            palindrome = english_letters_in_range[j:j + i]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes