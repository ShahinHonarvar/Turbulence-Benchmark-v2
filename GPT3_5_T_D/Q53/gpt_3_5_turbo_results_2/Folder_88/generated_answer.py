import re

def palindrome_of_length_at_least_n(string):
    pattern = '\x08([a-zA-Z]{27,})\x08'
    palindromes = set(re.findall(pattern, string, re.IGNORECASE))
    return palindromes