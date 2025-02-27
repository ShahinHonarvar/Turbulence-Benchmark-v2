def find_subset_of_length_n(A):
    return len({tuple(x) for x in itertools.combinations(A, 38)})