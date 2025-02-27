from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    result = set()
    for r in range(5, 0, -1):
        for p in permutations(s, r):
            w = ''.join(p)
            if w == w[::-1] and len(w) >= 5:
                result.add(w)
    return result