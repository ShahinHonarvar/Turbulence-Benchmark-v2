import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 111):
        for j in range(i, i + 112):
            if s[i:j + 1] == s[i:j + 1][::-1] and re.match('^[a-zA-Z]+$', s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes