from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 85:
        return 0
    elif len(elements) == 85:
        return 1
    else:
        return len(list(combinations(elements, 85)))