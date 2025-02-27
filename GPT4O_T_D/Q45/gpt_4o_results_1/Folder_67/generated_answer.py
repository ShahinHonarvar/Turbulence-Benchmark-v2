from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substr = s[2:7].lower()
    alpha_chars = [c for c in substr if c.isalpha()]
    if len(alpha_chars) < 5:
        return set()
    unique_palindromes = set()
    for p in permutations(alpha_chars, len(alpha_chars)):
        perm_str = ''.join(p)
        if len(perm_str) >= 5 and is_palindrome(perm_str):
            unique_palindromes.add(perm_str)
    return unique_palindromes