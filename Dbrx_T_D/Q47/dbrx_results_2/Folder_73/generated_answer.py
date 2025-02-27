import re
import string

def palindromes_of_specific_lengths(s):
    s = s[21:63].lower()
    english_letters = string.ascii_lowercase
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            if s[i:i + length] and s[i:i + length] == s[i:i + length][::-1] and all((c in english_letters for c in s[i:i + length])):
                palindromes.add(s[i:i + length])
    return palindromes