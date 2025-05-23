import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 180):
        substring = s[i:i + 181]
        if substring == substring[::-1] and re.match('^[a-z]+$', substring):
            palindromes.add(substring)
    return palindromes