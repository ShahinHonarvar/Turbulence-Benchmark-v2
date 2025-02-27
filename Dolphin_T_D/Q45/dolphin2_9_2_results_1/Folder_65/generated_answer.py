import itertools

def palindromes_between_indices(s):
    perm = set((''.join(i) for i in itertools.permutations(s[0:7].lower())))
    return set((w for w in perm if len(w) >= 5 and w == w[::-1]))