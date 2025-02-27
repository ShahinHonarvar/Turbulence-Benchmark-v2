import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 15):
        sub = s[i:i + 16]
        if re.match('^[a-z]+$', sub) and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes