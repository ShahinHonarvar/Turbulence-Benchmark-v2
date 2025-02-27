import itertools

def find_subset_of_length_n(input_set):
    if len(input_set) < 25:
        return 0
    return len(list(itertools.combinations(input_set, 25)))