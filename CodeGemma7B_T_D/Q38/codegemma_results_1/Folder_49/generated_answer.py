def find_subset_of_length_n(set):
    result = 0
    for subset in itertools.combinations(set, 68):
        result += 1
    return result