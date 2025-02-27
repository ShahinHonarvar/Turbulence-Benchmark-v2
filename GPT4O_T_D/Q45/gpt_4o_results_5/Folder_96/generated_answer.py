from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    alpha_only = ''.join(filter(str.isalpha, sub_str))
    perms = set((''.join(p) for p in permutations(alpha_only) if len(p) == len(alpha_only)))
    return {p for p in perms if len(p) >= 6 and is_palindrome(p)}