import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters = list(set(letters))
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes