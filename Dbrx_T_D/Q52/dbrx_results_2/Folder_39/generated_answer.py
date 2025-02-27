import re
from collections import defaultdict

def palindrome_of_length_n(s):

    def expand_around_center(s, left, right, is_odd):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            if is_odd:
                palindromes.add(s[left:right + 1])
            else:
                palindromes.add(s[left + 1:right + 1])
            left -= 1
            right += 1
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = ''.join((c for c in s if c in english_letters))
    palindromes = set()
    if len(s) < 59:
        return palindromes
    for i in range(len(s)):
        expand_around_center(s, i, i, True)
        expand_around_center(s, i, i + 1, False)
    return palindromes