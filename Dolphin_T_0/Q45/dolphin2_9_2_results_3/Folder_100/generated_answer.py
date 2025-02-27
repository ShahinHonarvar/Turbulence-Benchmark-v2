import itertools

def palindromes_between_indices(s):
    s = s[:6].lower()
    palindromes = set()
    for p in range(6, 0, -1):
        for t in itertools.permutations(s, p):
            for c in itertools.combinations(t, p // 2):
                s = ''.join(c) + ''.join(reversed(c))
                palindromes.add(s)
    return palindromes