from itertools import chain, combinations

def find_subset_of_length_n(elements):
    if len(elements) < 64:
        return 0
    elif len(elements) == 64:
        return 1
    else:
        return sum((1 for k in range(64, len(elements) + 1) for subset in combinations(elements, k) if len(subset) == 64))