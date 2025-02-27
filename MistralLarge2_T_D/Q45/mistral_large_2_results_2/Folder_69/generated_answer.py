import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:4] if c.isalpha()]
    permutations = set((''.join(p) for p in itertools.permutations(letters)))
    palindromes = set((p for p in permutations if len(p) >= 4 and p == p[::-1]))
    return palindromes