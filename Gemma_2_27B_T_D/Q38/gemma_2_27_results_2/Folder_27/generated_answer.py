from itertools import combinations

def find_subset_of_length_n(elements):
    n = 56
    return len([subset for subset in powerset(elements) if len(subset) == n])

def powerset(iterable):
    s = list(iterable)
    return (frozenset(c) for i in range(1 << len(s)) for c in combinations(s, i))