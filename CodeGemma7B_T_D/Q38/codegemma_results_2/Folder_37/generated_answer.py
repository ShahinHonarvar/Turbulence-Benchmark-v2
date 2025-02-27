def find_subset_of_length_n(set_of_element):
    n = 28
    count = 0
    for subset in itertools.combinations(set_of_element, n):
        count += 1
    return count