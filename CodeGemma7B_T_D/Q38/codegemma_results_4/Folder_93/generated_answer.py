def find_subset_of_length_n(a):
    b = 0
    for subset in itertools.combinations(a, 45):
        b += 1
    return b