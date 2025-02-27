from itertools import combinations

def find_subset_of_length_n(elements):
    return len([subsets for i in range(len(elements)) for subsets in combinations(elements, i) if len(subsets) == 7])