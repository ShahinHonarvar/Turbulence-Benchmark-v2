import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(10, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if re.match('^[a-z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes