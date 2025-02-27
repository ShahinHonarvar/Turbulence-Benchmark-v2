def find_subset_of_length_n(an_iterable):
    num_subsets = 0
    for subset in itertools.combinations(an_iterable, 752):
        num_subsets += 1
    return num_subsets