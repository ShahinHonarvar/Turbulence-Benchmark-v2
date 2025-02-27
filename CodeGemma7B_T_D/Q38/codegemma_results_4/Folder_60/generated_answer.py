from itertools import combinations

def find_subset_of_length_n(set):
    return len([comb for comb in combinations(set, 88)])