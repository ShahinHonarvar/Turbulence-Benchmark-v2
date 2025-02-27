def find_subset_of_length_n(s):
    return len([subset for n in range(len(s) + 1) if n == 31 for subset in itertools.combinations(s, n)])