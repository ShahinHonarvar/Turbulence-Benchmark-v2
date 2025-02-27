def find_subset_of_length_n(data):
    n = 53
    return len([subset for i in range(len(data)) for subset in itertools.combinations(data, i) if len(subset) == n])