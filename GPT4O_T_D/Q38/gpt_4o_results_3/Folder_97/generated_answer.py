import itertools

def find_subset_of_length_n(elements):
    if len(elements) < 219:
        return 0
    return len(list(itertools.combinations(elements, 219)))