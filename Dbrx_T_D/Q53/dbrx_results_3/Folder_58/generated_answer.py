import re
from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 147
    s = s.lower()
    s = re.sub('\\W+', '', s)
    len_s = len(s)
    if len_s < n:
        return palindromes
    for i in range(len_s - n + 1):
        sub_s = s[i:i + n]
        if is_palindrome(sub_s):
            palindromes.add(sub_s)
    return palindromes

def is_palindrome(s):
    return s == s[::-1]