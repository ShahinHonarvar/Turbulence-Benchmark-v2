def find_subset_of_length_n(my_set):
    return len({tuple(element) for element in itertools.combinations(my_set, 47)})