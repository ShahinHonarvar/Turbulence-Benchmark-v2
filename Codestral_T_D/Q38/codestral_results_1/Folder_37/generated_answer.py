from itertools import combinations

def find_subset_of_length_n(s, n=28):
    return len(list(combinations(s, n)))