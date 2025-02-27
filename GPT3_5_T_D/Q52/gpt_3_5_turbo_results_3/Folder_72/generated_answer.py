import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = '[a-z]{16}'
    palindromes = re.findall(pattern, string)
    return set(palindromes)