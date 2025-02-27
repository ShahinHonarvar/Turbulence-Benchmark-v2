from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[2:9] if c.isalpha()]
    if len(letters) < 7:
        return set()
    all_permutations = [''.join(p) for p in permutations(letters, 7)]
    return set((p for p in all_permutations if p == p[::-1]))