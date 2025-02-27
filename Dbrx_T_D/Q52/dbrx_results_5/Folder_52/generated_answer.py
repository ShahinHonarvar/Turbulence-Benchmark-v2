import re
import string

def palindrome_of_length_n(s):

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c.lower() in string.ascii_letters))
        return s == s[::-1]
    n = 423
    return {substr for i in range(len(s) - n + 1) for j in range(i, i + n) if is_palindrome(s[i:j + 1]) and s[i:j + 1].isalpha()}