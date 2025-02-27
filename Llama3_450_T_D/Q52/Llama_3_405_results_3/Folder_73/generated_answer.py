import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        if substring == substring[::-1] and re.match('^[a-z]+$', substring):
            palindromes.add(substring)
    return palindromes