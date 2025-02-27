from itertools import combinations

def find_subset_of_length_n(set1, n=19):
    return len(list(combinations(set1, n)))