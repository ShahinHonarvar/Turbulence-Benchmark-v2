import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = '(?=([a-z]{13,}))\\1'
    palindromes = set(re.findall(regex, s))
    return palindromes