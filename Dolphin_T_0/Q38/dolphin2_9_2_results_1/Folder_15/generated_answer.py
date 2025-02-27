def find_subset_of_length_n(s):
    count = 0
    for subset in itertools.combinations(s, 10):
        count += 1
    return count