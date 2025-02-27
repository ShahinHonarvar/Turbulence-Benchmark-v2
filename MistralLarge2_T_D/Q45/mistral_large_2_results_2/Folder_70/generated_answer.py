import itertools

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[1:7] if ch.isalpha()]
    permutations = set((''.join(p) for r in range(4, len(letters) + 1) for p in itertools.permutations(letters, r)))
    return {p for p in permutations if p == p[::-1]}