import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    a = re.findall('[a-z]{25,}', s)
    palindromes = set()
    for b in a:
        if b == b[::-1]:
            palindromes.add(b)
    return palindromes