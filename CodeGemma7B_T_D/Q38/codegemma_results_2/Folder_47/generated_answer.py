from itertools import combinations

def find_subset_of_length_n(a):
    return len(list(combinations(a, 34)))