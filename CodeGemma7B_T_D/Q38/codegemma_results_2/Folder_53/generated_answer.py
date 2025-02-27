from itertools import combinations

def find_subset_of_length_n(set):
    number_of_subsets = 0
    for subset in combinations(set, 73):
        number_of_subsets += 1
    return number_of_subsets