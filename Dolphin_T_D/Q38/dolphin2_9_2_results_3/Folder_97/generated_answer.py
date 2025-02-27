def find_subset_of_length_n(my_set):
    return len([s for s in chain.from_iterable((combinations(my_set, r) for r in range(len(my_set) + 1))) if len(s) == 219])