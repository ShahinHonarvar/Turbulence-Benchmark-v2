from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    return sum((len(combination) == 21 for combination in combinations(set_of_elements, 21)))