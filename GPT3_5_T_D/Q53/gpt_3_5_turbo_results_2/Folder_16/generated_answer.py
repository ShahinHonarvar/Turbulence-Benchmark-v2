import re

def palindrome_of_length_at_least_n(string):
    n = 119
    pattern = '\x08\\w{' + str(n) + ',}\x08'
    matches = set(re.findall(pattern, string, flags=re.I))
    palindromes = set(filter(lambda x: x.lower() == x.lower()[::-1], matches))
    return palindromes