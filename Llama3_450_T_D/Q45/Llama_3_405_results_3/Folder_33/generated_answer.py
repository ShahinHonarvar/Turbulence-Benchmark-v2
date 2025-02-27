import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[7:10] if c.isalpha()]
    letters = ''.join(chars).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes