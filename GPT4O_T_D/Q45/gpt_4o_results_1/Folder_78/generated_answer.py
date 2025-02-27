from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    if len(s) < 9:
        return set()
    segment = s[6:9]
    segment_letters = [char for char in segment if char.isalpha()]
    if len(segment_letters) < 3:
        return set()
    perms = set((''.join(p) for p in permutations(segment_letters) if len(p) >= 3))
    return {perm for perm in perms if is_palindrome(perm)}