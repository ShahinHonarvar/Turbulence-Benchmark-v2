from itertools import chain, combinations

def find_subset_of_length_n(s, n):
    return len(list(filter(lambda x: len(x) == n, chain.from_iterable((combinations(s, r) for r in range(len(s) + 1))))))