from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 57:
        return 0
    if len(elements) == 57:
        return 1 if len(set(elements)) == 57 else 0
    return sum((1 for subset in combinations(elements, 57) if len(set(subset)) == 57))