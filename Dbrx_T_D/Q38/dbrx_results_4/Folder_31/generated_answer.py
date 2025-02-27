from itertools import chain, combinations

def find_subset_of_length_n(elements, n):
    return len(list(filter(lambda x: len(x) == n, chain.from_iterable((combinations(elements, r) for r in range(len(elements) + 1))))))