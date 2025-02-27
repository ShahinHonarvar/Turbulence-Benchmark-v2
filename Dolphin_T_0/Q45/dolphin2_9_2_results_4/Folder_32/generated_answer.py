import itertools

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[1:8] if c.isalpha()])
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in itertools.permutations(letters, i):
            for p in [''.join(p) for p in itertools.product(*[itertools.combinations_with_replacement(p, 2) for p in set(perm)]) if p[::-1] == p and len(p) >= 5]:
                palindromes.add(p)
    return palindromes