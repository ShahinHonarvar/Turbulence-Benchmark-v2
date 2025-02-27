from itertools import combinations

def find_subset_of_length_n(given_set):
    number_of_subsets = 0
    for subset in combinations(given_set, 16):
        number_of_subsets += 1
    return number_of_subsets