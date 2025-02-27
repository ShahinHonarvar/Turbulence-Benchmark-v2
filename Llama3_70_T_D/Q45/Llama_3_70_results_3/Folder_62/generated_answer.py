from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[:9].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 7:
        return set()
    result = set()
    for combo in combinations(letters, 7):
        for perm in permutations(combo):
            p = ''.join(perm)
            if p == p[::-1]:
                result.add(p)
    for combo in combinations(letters, 8):
        for perm in permutations(combo):
            p = ''.join(perm)
            if p == p[::-1]:
                result.add(p)
    for combo in combinations(letters, 9):
        for perm in permutations(combo):
            p = ''.join(perm)
            if p == p[::-1]:
                result.add(p)
    return result