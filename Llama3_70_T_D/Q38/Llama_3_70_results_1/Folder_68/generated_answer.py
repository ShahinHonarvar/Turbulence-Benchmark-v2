import itertools

def find_subset_of_length_n(s):
    return sum((1 for _ in itertools.combinations(s, 3)))