import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 68
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
                palindromes.add(substring)
    return palindromes