from itertools import combinations

def find_subset_of_length_n(elements, n=60):
    if n != 60:
        raise ValueError('Function only supports finding subsets of length 60.')
    return len(list(combinations(elements, n)))