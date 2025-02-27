import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 25, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                if all((c.isalpha() for c in sub)):
                    palindromes.add(sub)
    return palindromes