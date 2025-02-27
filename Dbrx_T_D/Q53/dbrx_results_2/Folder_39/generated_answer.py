import re
import string

def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.lower() in string.ascii_letters))
    palindromes = set()
    for i in range(len(s) - 68):
        for j in range(i + 69, len(s) + 1, 2):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes