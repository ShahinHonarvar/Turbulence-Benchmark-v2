import re
import string

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 22):
        for j in range(i, i + 23):
            if s[i:j + 1] and s[i:j + 1] == s[i:j + 1][::-1] and s.isalpha(s[j]):
                palindromes.add(s[i:j + 1])
    return palindromes