from itertools import combinations

def find_subset_of_length_n(the_set):
    return len(list(combinations(the_set, 93)))