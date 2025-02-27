import itertools

def palindromes_between_indices(text):
    letters = set((c.lower() for c in text[5:7] if c.isalpha()))
    if len(letters) < 3:
        return set()
    return set([''.join(p) for p in itertools.permutations(letters, 3)])