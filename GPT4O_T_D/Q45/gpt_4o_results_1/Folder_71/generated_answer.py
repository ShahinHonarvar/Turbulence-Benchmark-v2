from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substr = s[1:4].lower()
    letters = [char for char in substr if char.isalpha()]
    if len(letters) < 4:
        return set()
    perms = set((''.join(p) for length in range(4, len(letters) + 1) for p in permutations(letters, length)))
    return {p for p in perms if is_palindrome(p)}