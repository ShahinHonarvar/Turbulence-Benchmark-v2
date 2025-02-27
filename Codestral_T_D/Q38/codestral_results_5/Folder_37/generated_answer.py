import itertools

def find_subset_of_length_n(s, n=28):
    return len(list(itertools.combinations(s, n)))