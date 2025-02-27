from collections import defaultdict

def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    start, end = (155, 283)
    min_len, max_len = (104, 120)
    palindromes = set()
    for i in range(start, end + 1 - min_len + 1):
        for j in range(min_len, max_len + 1):
            if is_palindrome(s[i:i + j]):
                palindromes.add(s[i:i + j])
    return palindromes