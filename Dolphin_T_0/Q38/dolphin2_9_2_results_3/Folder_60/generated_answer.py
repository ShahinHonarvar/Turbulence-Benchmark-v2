def find_subset_of_length_n(s):
    return len([comb for comb in itertools.combinations(s, 88)])