def find_subset_of_length_n(elements):
    return len({frozenset(comb) for comb in itertools.combinations(elements, 15)})