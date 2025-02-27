import itertools

def palindromes_between_indices(s):
    s = s[1:10]
    s = ''.join((c for c in s if c.isalpha())).lower()
    n = len(s)
    palindromes = set()
    for p in range(7, n + 1):
        for subset in itertools.combinations(s, p):
            for perm in itertools.permutations(subset):
                if ''.join(perm) == ''.join(reversed(''.join(perm))):
                    palindromes.add(''.join(perm))
    return palindromes