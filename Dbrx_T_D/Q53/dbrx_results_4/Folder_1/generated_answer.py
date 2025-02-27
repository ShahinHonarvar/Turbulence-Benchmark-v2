from collections import defaultdict
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 29
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring.replace(substring, substring[::2], 1)):
            palindromes.add(substring)
    return palindromes

def is_palindrome(s):
    s = re.sub('\\W+', '', s)
    if s == s[::-1]:
        return True
    return False