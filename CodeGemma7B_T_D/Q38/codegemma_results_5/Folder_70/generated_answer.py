from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    for subset in combinations(set_of_elements, 534):
        number_of_subsets += 1
    return number_of_subsets