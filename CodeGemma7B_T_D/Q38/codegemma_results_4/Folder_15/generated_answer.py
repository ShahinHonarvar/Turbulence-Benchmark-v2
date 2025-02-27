def find_subset_of_length_n(set):
    result = []
    for subset in itertools.combinations(set, 10):
        result.append(subset)
    return len(result)