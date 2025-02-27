import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 275):
        substring = s[i:i + 276].lower()
        if substrlice == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
            palindromes.add(substring)
    return palindromes