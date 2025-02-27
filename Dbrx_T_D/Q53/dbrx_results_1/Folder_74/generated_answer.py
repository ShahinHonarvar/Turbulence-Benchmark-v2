import re
import string

def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.lower() in string.ascii_letters))
    palindromes = set()
    for i in range(len(s) - 56):
        for j in range(57):
            if i + j > len(s):
                break
            substring = s[i:i + j]
            if len(substring) < 57:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes