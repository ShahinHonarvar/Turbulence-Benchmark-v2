from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    middle_substring = s[2:6]
    letters = [c.lower() for c in middle_substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        if is_palindrome(perm_str):
            palindromes.add(perm_str)
    return {p for p in palindromes if len(p) >= 5}