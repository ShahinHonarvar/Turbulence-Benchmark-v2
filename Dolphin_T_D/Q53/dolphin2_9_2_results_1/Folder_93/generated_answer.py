import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(90, len(string) + 1):
        for j in range(len(string) - i + 1):
            word = string[j:j + i]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word.lower())
    return palindromes