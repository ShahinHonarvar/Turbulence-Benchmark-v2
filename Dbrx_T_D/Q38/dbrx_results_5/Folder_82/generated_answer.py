import itertools

def find_subset_of_length_n(elements_set, n=83):
    if len(elements_set) < n:
        return 0
    else:
        return len(list(itertools.combinations(elements_set, n)))