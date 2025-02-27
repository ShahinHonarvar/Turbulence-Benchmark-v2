import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:4].lower()
    letters = defaultdict(int)
    for char in s:
        letters[char] += 1
    palindromes = set()
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            curr = s[j:j + i]
            if len(curr) >= 3 and is_palindrome(curr) and is_case_insensitive_palindrome(curr):
                count = 0
                for k in curr:
                    count += letters[k] - letters[k, count % 2]
                if count % 2 == 0:
                    palindromes.add(curr)
    return palindromes

def is_palindrome(s):
    return s == s[::-1]

def is_case_insensitive_palindrome(s):
    return len(s) <= 1 or s.lower() == s.lower()[::-1]