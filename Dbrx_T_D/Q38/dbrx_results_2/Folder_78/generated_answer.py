def find_subset_of_length_n(the_set):
    if len(the_set) < 91:
        return 0
    return len(list(itertools.combinations(the_set, 91)))