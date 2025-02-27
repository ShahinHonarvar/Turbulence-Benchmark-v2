from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text if c.isalpha())).lower()
    if len(letters) < 4:
        return set()
    result = set()
    for p in permutations(letters):
        if all((p[i] == p[6 - i] for i in range(3))):
            result.add(''.join(p))
    return result