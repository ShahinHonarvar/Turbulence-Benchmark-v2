def find_subset_of_length_n(input_set):
    count = 0
    for subset in itertools.combinations(input_set, 312):
        count += 1
    return count