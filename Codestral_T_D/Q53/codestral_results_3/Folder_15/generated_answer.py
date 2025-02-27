import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for match in re.finditer('\\\\b\\\\w+\\\\b', string):
        word = match.group()
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes