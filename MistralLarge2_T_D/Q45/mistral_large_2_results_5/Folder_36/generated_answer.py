from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[5:9] if c.isalpha()]
    letters_set = set((''.join(perm) for perm in permutations(letters) if perm == perm[::-1] and len(perm) >= 3))
    return letters_set