import re
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for n in range(138, len(s) + 1):
        for i in range(len(s) - n + 1):
            candidate = s[i:i + n]
            if candidate == candidate[::-1] and candidate.translate(str.maketrans('', '', string.punctuation)).isalpha():
                palindromes.add(candidate)
    return palindromes