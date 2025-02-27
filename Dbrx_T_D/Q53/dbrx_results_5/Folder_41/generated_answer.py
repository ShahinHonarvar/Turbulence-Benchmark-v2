import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 27):
        for j in range(i, len(s) - i):
            if len(s[i:j + 1]) < 28:
                continue
            if s[i:j + 1] == s[i:j + 1][::-1].lower() and re.match('^[a-zA-Z]*$', s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes