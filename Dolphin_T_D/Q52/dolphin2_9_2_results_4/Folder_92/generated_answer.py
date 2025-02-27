import re

def palindrome_of_length_n(s):
    s = s.lower()
    pattern = '\\b(\\w){10}\\b'
    palindromes = set(re.findall(pattern, s))
    return palindromes