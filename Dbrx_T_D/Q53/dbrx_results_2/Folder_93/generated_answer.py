import re
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 89):
        for j in range(i + 45, i + 91):
            if s[i:j] == s[i:j][::-1] and s[i:j] not in palindromes:
                palindromes.add(s[i:j])
    return palindromes