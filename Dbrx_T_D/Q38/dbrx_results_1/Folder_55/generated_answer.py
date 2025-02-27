def find_subset_of_length_n(collection, n=21):
    subset_count = 0
    for subset in itertools.combinations(collection, n):
        subset_count += 1
    return subset_count