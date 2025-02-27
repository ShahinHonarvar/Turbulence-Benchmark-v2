def find_subset_of_length_n(set1):
    return len(set([subset for i in range(len(set1) + 1) for subset in itertools.combinations(set1, i) if len(subset) == 8]))