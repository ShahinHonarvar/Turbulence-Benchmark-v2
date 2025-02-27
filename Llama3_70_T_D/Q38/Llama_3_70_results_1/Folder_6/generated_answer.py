def find_subset_of_length_n(input_set):
    n = 89
    return len([subset for subset in __import__('itertools').chain.from_iterable((__import__('itertools').combinations(input_set, r) for r in range(n, n + 1)))])