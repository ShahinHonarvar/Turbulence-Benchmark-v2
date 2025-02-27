import itertools

def palindromes_between_indices(s):
    s = s[2:7]
    palindromes = set()
    for L in range(4, len(s) + 1):
        for perm in itertools.permutations(s, L):
            p = ''.join(perm).lower()
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes