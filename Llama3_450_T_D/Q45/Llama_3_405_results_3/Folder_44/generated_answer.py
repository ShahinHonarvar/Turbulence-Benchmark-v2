import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for subset in itertools.combinations(letters, r):
            for p in itertools.permutations(subset):
                p = ''.join(p)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes