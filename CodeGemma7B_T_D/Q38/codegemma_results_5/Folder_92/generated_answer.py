from itertools import combinations

def find_subset_of_length_n(set_input):
    return len([list(x) for x in combinations(set_input, 0)])