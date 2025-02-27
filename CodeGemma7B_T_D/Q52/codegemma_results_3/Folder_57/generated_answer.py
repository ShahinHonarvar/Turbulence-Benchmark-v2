import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower() and len(substring) == 92:
                palindromes.add(substring)
    return palindromes