from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) <= 3:
        return set()
    sub_str = ''.join([c for c in s[3:7] if c.isalpha()])
    palindromes = set()
    for perm in permutations(sub_str):
        perm_str = ''.join(perm)
        if is_palindrome(perm_str) and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes