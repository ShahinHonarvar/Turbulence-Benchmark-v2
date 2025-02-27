from itertools import combinations

def find_subset_of_length_n(s):
    return len([list(i) for i in combinations(s, 60)])