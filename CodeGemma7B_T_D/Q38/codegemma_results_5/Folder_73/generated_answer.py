from itertools import combinations

def find_subset_of_length_n(elements):
    num_subsets = 0
    for subset in combinations(elements, 41):
        num_subsets += 1
    return num_subsets