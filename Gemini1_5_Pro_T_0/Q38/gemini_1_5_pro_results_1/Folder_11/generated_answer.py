def find_subset_of_length_n(s):
    return len([x for i in range(len(s) + 1) for x in itertools.combinations(s, i) if len(x) == 77])