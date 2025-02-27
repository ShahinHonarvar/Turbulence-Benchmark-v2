import re
from collections import defaultdict

def palindrome_of_length_n(s):
    palindromes = set()
    n = 18
    if len(s) < n:
        return palindromes
    s = s.lower()
    table = defaultdict(set)
    for i in range(len(s) - n + 1):
        word = s[i:i + n]
        if word == word[::-1]:
            table[tuple(word)].add(word)
            palindromes.add(word)
    return palindromes