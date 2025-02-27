import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(80, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            word = s[i:i + length]
            if word == word[::-1].lower():
                palindromes.add(word.lower())
    return palindromes