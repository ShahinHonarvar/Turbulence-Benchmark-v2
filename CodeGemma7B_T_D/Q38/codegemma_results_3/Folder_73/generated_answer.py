def find_subset_of_length_n(set_):
    count = 0
    for subset in itertools.combinations(set_, 41):
        count += 1
    return count