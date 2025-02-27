from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    s = s.lower()
    segment = ''.join([c for c in s[:6] if c.isalpha()])
    palindromes = set()
    unique_perms = set([''.join(p) for p in permutations(segment)])
    for perm in unique_perms:
        half = len(perm) // 2
        for i in range(half, len(perm) + 1):
            if perm[:i] == perm[i:][::-1]:
                palindromes.add(perm)
                break
    return {p for p in palindromes if len(p) >= 4}