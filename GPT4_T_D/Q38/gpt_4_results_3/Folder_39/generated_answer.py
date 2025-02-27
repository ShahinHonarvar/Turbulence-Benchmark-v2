import itertools

def find_subset_of_length_n(idx_set):
    return len(list(itertools.combinations(idx_set, 59)))