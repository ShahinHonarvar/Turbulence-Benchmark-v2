import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 72):
        substring = ''.join((c.lower() for c in s[i:i + 73] if c.isalpha()))
        if substring and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes