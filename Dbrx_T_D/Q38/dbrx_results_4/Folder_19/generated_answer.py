from itertools import combinations

def find_subset_of_length_n(s):
    n = len(s)
    k = 13
    if n < k:
        return 0
    else:
        return len(list(combinations(s, k)))