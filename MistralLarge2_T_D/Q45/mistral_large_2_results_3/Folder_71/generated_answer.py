import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:4] if c.isalpha()]
    if len(letters) < 4:
        return set()
    permutations = set((''.join(p) for p in itertools.permutations(letters, len(letters))))
    palindromes = set((p for p in permutations if p == p[::-1] and len(p) >= 4))
    return palindromes