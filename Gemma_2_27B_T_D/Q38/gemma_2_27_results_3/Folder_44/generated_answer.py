def find_subset_of_length_n(s):
    return len([subset for i in range(len(s)) for subset in itertools.combinations(s, 30) if len(subset) == 30])