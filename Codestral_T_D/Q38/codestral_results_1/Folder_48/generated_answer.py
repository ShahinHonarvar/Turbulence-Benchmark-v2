from itertools import combinations

def find_subset_of_length_n(s):
    if len(s) == 793:
        return 1
    elif len(s) > 793:
        return len(list(combinations(s, 793)))
    else:
        return 0