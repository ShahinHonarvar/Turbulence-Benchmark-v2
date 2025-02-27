import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set(re.findall('\\\\b(\\\\w{67,?})\\\\b', s))
    return palindromes