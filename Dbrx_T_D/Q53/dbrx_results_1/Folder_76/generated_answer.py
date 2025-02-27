import re
import string

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 136):
        for j in range(i, i + 137):
            candidate = text[i:j + 1]
            if candidate.lower().isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 137}