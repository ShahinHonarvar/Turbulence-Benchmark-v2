from itertools import permutations

def palindromes_between_indices(text):
    letters = [t for t in text[2:9] if t.isalpha()]
    return set((p for p in {''.join(p) for p in permutations(letters) if len(p) >= 6 and p == p[::-1]} | {''.join(p) for p in permutations(letters) if len(p) >= 6 and p == p[::-1].lower()}))