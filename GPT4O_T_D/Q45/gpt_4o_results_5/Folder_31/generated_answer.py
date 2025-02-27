from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    substr = ''.join([ch for ch in s[1:9] if ch.isalpha()])
    palindromes = set()
    for perm in permutations(substr):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and is_palindrome(perm_str):
            palindromes.add(perm_str)
    return palindromes