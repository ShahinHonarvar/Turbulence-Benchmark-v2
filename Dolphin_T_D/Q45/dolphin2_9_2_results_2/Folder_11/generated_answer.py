import itertools

def palindromes_between_indices(s):
    palindromes = set()
    substring = ''.join(s[3:8])
    for p in range(4, len(substring) + 1):
        for perm in itertools.permutations(list(substring), p):
            for w in itertools.product(*zip(perm, repeat(1), perm[::-1])):
                palindromes.add(''.join(w).lower())
    return palindromes