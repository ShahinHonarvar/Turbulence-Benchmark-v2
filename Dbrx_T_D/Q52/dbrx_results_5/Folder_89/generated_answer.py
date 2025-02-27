import re
from collections import defaultdict

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 36):
        substr = s[i:i + 37]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes

def is_palindrome(s):
    s = re.sub('[^a-z]', '', s)
    return s == s[::-1]