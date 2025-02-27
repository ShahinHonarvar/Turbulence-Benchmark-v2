def find_subset_of_length_n(set):
    size = 872
    count = 0
    for subset in itertools.combinations(set, size):
        count += 1
    return count