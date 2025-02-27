from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    return set((p for p in {''.join(x) for x in permutations(letters)} if len(p) >= 5 and p == p[::-1]))