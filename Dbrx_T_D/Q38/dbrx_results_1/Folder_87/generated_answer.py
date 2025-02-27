from itertools import chain, combinations

def find_subset_of_length_n(s):
    return len(list(chain.from_iterable(combinations(s, 96))))