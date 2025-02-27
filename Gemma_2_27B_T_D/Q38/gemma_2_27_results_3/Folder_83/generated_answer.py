from itertools import chain, combinations

def find_subset_of_length_n(elements):
    n = 95
    return sum((1 for subset in powerset(elements) if len(subset) == n))

def powerset(iterable):
    return chain.from_iterable((combinations(iterable, r) for r in range(len(iterable) + 1)))