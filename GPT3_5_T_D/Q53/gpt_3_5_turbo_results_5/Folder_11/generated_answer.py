import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set(re.findall('(?=(\x08[a-zA-Z]{54,}\x08))(?i)', string))
    return palindromes