from itertools import permutations

def permutations_between_indices(text):
    text = text.lower()
    ltrs = ''.join(set(text[3:10]))
    if len(ltrs) < 3:
        return set()
    return {''.join(p) for p in permutations(ltrs) if ''.join(p) == ''.join(p)[::-1]}