import re

def palindrome_of_length_n(s):
    s = s.lower()
    pattern = '[a-z]{48}'
    palindromes = set(re.findall(pattern, s))
    result = set()
    for p in palindromes:
        if p == p[::-1]:
            result.add(p)
    return result