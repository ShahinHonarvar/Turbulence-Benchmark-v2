def find_subset_of_length_n(s):
    return len(list(filter(lambda x: len(x) == 86, itertools.combinations(s, range(0, 87)))))