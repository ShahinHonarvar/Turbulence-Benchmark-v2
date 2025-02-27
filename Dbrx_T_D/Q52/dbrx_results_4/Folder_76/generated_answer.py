import re

def palindrome_of_length_n(s):
    n = 257
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
            palindromes.add(substring)
    return palindromes