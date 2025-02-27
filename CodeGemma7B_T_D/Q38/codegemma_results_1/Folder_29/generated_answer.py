def find_subset_of_length_n(a):
    return len([list(i) for i in itertools.combinations(a, 19)])