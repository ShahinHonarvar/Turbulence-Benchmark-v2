def find_subset_of_length_n(input_set):
    count = 0
    for i in range(len(input_set)):
        for subset in itertools.combinations(input_set, 1):
            count += 1
    return count