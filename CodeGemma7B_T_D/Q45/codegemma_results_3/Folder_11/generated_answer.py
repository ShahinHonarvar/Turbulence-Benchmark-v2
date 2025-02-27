from itertools import permutations
    from collections import defaultdict

def palindromes_between_indices(text):
    i = 0
    d = defaultdict(list)
    for c in text.lower():
        if 'a' <= c <= 'z' and i > 2 and (i < 8):
            d[c].append(i)
        i += 1
    if not d:
        return set()
    t = ''.join(sorted(d))
    if len(t) < len(text[3:8]):
        return set()
    p = sorted(list(permutations(t)))
    return {''.join(list(q)) for q in p if q == q[::-1]}