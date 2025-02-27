def find_subset_of_length_n(elements):
    return len([subset for subset in [set(comb) for comb in itertools.combinations(elements, 3)]])