from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[4:10]
    substr = ''.join(filter(str.isalpha, substr))
    if len(substr) < 6:
        return set()
    perm = set((''.join(p) for p in permutations(substr) if is_palindrome(''.join(p))))
    return {p for p in perm if len(p) >= 6}