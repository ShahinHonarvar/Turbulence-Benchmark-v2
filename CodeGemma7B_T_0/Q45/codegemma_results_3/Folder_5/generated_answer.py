from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    text = text[4:9]
    if not text or len(text) < 4:
        return set()
    return {''.join(p) for p in permutations(text) if p == p[::-1]}