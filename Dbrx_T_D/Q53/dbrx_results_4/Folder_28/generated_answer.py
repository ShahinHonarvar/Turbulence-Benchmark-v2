import re
import string

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    s = ''.join((c for c in s if c in string.ascii_letters))
    for i in range(len(s) - 41):
        for j in range(i + 21, len(s) - i):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes