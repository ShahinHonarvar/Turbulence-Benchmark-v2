from itertools import permutations

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def palindromes_between_indices(s):
    allowed_chars = set(s[3:7])
    permutations_set = set((''.join(permutation) for permutation in permutations(allowed_chars, 3)))
    return {permutation for permutation in permutations_set if is_palindrome(permutation)}