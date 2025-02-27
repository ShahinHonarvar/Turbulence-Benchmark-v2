from itertools import combinations

def find_subset_of_length_n(elements):
    count = 0
    if len(elements) >= 49:
        count = len(list(combinations(elements, 49)))
    return count