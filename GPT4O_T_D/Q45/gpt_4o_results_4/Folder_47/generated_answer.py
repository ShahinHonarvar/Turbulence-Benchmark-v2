from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = ''.join([c.lower() for c in s[3:8] if c.isalpha()])
    if len(substring) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(substring)):
        perm_str = ''.join(perm)
        if is_palindrome(perm_str) and len(perm_str) >= 5:
            palindromes.add(perm_str)
    return palindromes