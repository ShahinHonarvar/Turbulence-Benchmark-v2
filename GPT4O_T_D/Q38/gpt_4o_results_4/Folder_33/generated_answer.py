import itertools

def find_subset_of_length_n(s):
    if len(s) < 372:
        return 0
    return len(list(itertools.combinations(s, 372)))