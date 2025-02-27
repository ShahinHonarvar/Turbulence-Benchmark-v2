def find_subset_of_length_n(s):
    return len([subset for subset in set(itertools.combinations(s, 360))])