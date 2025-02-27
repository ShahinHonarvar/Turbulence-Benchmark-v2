def find_subset_of_length_n(a_set, n=16):
    return sum((1 for subset in itertools.combinations(a_set, n)))