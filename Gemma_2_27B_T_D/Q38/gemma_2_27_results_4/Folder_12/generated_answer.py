def find_subset_of_length_n(s):
    return len([subset for subset in [list(set) for set in (set(x) for x in itertools.combinations(s, 27))]])