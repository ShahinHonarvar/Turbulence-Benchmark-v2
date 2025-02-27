import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
            palindromes.add(substring)
    return palindromes