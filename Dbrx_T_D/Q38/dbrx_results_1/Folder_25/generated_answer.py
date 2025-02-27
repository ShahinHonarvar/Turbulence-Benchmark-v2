import itertools

def find_subset_of_length_n(elements_set, n=90):
    if not isinstance(elements_set, set) or len(elements_set) < n:
        return 0
    return len(list(itertools.combinations(elements_set, n)))