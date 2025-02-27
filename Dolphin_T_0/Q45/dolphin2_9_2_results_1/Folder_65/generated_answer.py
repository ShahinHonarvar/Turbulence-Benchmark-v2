import itertools

def palindromes_between_indices(s):
    s = s[:7].lower()
    palindromes = set()
    for L in range(5, len(s) + 1):
        for subset in itertools.combinations(s, L):
            subset = ''.join(sorted(subset))
            subset_permutations = [''.join(p) for p in itertools.permutations(subset)]
            subset_palindromes = [p for p in subset_permutations if p == p[::-1] and len(p) >= 5]
            palindromes.update(subset_palindromes)
    return palindromes