import re

def palindrome_of_length_n(string):
    palindromes = set()
    substrings = re.findall('\\\\b\\\\w{173}\\\\b', string.lower())
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes