from itertools import combinations

def find_subset_of_length_n(args):
    return len([x for x in combinations(args, 77)])