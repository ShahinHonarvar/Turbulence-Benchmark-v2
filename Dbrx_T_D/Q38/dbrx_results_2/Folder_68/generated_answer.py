def find_subset_of_length_n(elements, n=3):
    return len(list((subset for subset in itertools.combinations(elements, n))))