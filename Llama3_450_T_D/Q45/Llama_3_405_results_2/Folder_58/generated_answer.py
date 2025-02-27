from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in combinations(letters, r):
            for p in permutations(combo):
                p = ''.join(p)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes