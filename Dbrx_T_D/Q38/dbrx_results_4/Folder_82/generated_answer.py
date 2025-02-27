from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 83:
        return 0
    elif len(elements) == 83:
        return 1
    else:
        subsets = [x for x in combinations(elements, 83)]
        return len(subsets)