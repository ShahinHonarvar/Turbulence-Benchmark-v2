import re

def palindrome_of_length_n(s):
    s = s.lower()
    n = 27
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and re.fullmatch('[a-zA-Z]*', substring):
            palindromes.add(substring)
    return palindromes