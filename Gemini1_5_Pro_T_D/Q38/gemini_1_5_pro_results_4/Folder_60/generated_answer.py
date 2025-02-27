from itertools import chain, combinations

def find_subset_of_length_n(set_of_elements):
    return len(set([subset for subset in powerset(set_of_elements) if len(subset) == 88]))

def powerset(s):
    return list(chain.from_iterable((combinations(s, r) for r in range(len(s) + 1))))