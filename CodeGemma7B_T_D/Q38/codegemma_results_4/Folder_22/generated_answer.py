import itertools

def find_subset_of_length_n(elements):
    result = itertools.combinations(elements, 72)
    return len(list(result))