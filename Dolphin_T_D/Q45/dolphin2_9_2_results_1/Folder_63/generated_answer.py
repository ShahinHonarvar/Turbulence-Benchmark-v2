from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    perms = [''.join(p) for p in permutations(s[:4].lower())]
    for i in range(3, len(s[:4])):
        for perm in perms:
            if all((perm[j] == perm[~j] for j in range(i + 1))):
                palindromes.add(perm)
    return palindromes