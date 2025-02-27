import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(87, len(s) + 1):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and re.match('^[a-z]+$', sub):
                palindromes.add(sub)
    return palindromes