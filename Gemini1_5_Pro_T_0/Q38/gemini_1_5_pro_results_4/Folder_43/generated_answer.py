import itertools

def find_subset_of_length_n(set_of_elements):
    n = 29
    if len(set_of_elements) < n:
        return 0
    elif len(set_of_elements) == n:
        return 1
    else:
        return sum((1 for subset in itertools.combinations(set_of_elements, n)))