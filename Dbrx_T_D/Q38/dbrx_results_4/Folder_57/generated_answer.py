from itertools import combinations

def find_subset_of_length_n(elements, n=92):
    if len(elements) < n:
        raise ValueError('The size of the set is less than the desired subset length.')
    return len(list(combinations(elements, n)))