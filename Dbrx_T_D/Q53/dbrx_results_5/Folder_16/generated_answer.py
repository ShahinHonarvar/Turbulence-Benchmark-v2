import re
from collections import defaultdict

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=119):
    s = s.lower()
    s = re.sub('\\W+', '', s)
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i, length):
            if is_palindrome(s[i:j + 1]) and j - i + 1 >= n:
                palindromes.add(s[i:j + 1])
    return palindromes