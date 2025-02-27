import re

def palindrome_of_length_n(s):
    s = s.lower()
    regex = '(?=([a-z]{19}))'
    palindromes = set()
    for match in re.finditer(regex, s):
        p = match.group(1)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes