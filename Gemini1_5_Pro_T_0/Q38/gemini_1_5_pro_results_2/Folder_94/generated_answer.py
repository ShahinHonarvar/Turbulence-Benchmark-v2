from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    return len({subset for subset in powerset(set_of_elements) if len(subset) == 93})

def powerset(s):
    return {frozenset(subset) for i in range(len(s) + 1) for subset in combinations(s, i)}