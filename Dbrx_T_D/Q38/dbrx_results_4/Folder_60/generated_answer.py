import itertools

def find_subset_of_length_n(elements, n):
    if n != 88:
        raise ValueError('Function is intended to find subsets of size 88')
    return len(list(itertools.combinations(elements, 88)))