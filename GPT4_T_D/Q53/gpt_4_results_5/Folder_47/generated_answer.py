import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    words = re.findall('\x08\\w+\x08', string)
    palindromes = {word for word in words if len(word) >= 77 and word == word[::-1]}
    return palindromes