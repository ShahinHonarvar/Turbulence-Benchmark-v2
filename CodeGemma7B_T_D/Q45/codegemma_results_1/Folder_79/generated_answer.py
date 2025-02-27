import itertools

def palindromes_between_indices(s):
    indices = [1, 2, 3, 4, 5, 6, 7]
    letters = sorted(set([c.lower() for c in s[max(indices):min(indices) + 1]]))
    if letters:
        return set([''.join(p) for p in itertools.permutations(letters)])
    return set()