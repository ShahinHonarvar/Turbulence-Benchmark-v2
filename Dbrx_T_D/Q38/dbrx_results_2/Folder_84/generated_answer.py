def find_subset_of_length_n(elements):
    subsets = {frozenset(fsubset) for length in range(1, 873) for fsubset in itertools.combinations(elements, length)}
    return sum((1 for subset in subsets if len(subset) == 872))