from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    pals = set()
    for p in permutations(letters, 5):
        candidate = ''.join(p)
        if is_palindrome(candidate):
            pals.add(candidate)
    return pals