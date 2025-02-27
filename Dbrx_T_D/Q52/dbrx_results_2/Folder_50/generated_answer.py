import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 40 + 1):
        substring = s[i:i + 40]
        if substring == substring[::-1] and re.fullmatch('[a-zA-Z]*$', substring):
            palindromes.add(substring)
    return palindromes