import itertools
    from collections import Counter

def palindromes_between_indices(S):
    palindromes = []
    for p in range(4, len(S) + 1):
        for subset in itertools.combinations(S, p):
            if Counter(subset) == Counter(subset[::-1]):
                palindromes.append(''.join(sorted(subset)))
    return set(palindromes)