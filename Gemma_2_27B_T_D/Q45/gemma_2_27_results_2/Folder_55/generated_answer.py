from itertools import permutations

def palindromes_between_indices(text):
    letters = set((text[i] for i in range(3) if text[i].isalpha()))
    return {''.join(p) for p in permutations(letters) if len(p) >= 3 and ''.join(p).lower() == ''.join(p)[::-1].lower()}