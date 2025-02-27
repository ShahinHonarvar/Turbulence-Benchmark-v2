import re
import string

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 139):
        for j in range(i + 70, min(len(s), i + 140) + 1):
            if s[i:j + 1] and s[i:j + 1] == s[i:j + 1][::-1] and all((c in string.ascii_letters for c in s[i:j + 1])):
                palindromes.add(s[i:j + 1])
    return palindromes