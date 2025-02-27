import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha() and c.isascii()]
    if len(letters) < 5:
        return set()
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes