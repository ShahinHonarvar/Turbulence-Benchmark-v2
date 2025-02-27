import itertools

def find_subset_of_length_n(elements):
    combinations = list(itertools.combinations(elements, 51))
    return len(combinations)