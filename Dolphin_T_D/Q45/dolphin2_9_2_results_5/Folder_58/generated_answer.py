import itertools

def palindromes_between_indices(s):
    s = s[:7].lower()
    return set((w for w in itertools.starmap(''.join, itertools.combinations_with_replacement(s, 3)) if w == w[::-1] and len(w) >= 6))