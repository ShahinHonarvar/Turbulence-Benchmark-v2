def find_subset_of_length_n(s):
    n = 793
    return len([subset for subset in __import__('itertools').chain.from_iterable((__import__('itertools').combinations(s, r) for r in range(n + 1))) if len(subset) == n])