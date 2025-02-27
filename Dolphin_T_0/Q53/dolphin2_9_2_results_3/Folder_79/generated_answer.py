import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 16):
        if s[i:i + 17] == s[i:i + 17][::-1]:
            palindromes.add(s[i:i + 17])
    return palindromes