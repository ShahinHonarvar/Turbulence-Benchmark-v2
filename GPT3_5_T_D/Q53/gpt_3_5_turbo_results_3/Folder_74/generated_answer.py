import re

def palindrome_of_length_at_least_n(string):
    pattern = '\x08[a-zA-Z]{57,}\x08'
    palindromes = set(re.findall(pattern, string.lower()))
    return palindromes