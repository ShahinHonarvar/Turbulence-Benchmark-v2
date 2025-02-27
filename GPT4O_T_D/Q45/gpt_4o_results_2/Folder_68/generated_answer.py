from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    alpha_substring = ''.join([char.lower() for char in s[1:9] if char.isalpha()])
    if len(alpha_substring) < 4:
        return set()
    perms = set((''.join(p) for p in permutations(alpha_substring) if is_palindrome(p) and len(p) >= 4))
    return perms