import itertools

def find_subset_of_length_n(s):
    if len(s) < 97:
        return 0
    return len(list(itertools.combinations(s, 97)))