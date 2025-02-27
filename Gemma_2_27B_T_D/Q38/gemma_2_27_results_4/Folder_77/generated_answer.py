def find_subset_of_length_n(data):
    return len([subset for i in range(len(data)) for subset in itertools.combinations(data, 360)])