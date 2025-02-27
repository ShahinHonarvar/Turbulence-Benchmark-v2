import re

def palindrome_of_length_n(s):
    n = 416
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and re.match('^[a-z]*$', substring):
            palindromes.add(substring)
    return palindromes