from itertools import combinations

def find_subset_of_length_n(elements):
    return len([comb for comb in combinations(elements, 87)])