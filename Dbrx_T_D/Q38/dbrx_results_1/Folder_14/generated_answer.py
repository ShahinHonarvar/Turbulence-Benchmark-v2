def find_subset_of_length_n(s, n=17):
    return sum((1 for i in itertools.combinations(s, n)))