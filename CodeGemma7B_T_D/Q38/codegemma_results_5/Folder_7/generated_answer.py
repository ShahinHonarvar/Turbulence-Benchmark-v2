from itertools import combinations

def find_subset_of_length_n(set):
    return len([ele for ele in combinations(set, 180)])