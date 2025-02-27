from itertools import combinations

def find_subset_of_length_n(s):
    n = 3
    if len(s) < n:
        return 0
    else:
        return len(list(combinations(s, n)))