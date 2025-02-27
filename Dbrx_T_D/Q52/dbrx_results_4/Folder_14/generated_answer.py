import re
from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 63
    if len(s) < n:
        return palindromes
    for i in range(len(s) - n + 1):
        for j in range(i, i + n):
            if s[i:j + 1] and s[i:j + 1] == s[i:j + 1][::-1] and re.fullmatch('[a-zA-Z]*', s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes