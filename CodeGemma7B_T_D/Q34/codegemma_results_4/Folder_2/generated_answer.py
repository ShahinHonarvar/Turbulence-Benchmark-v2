from itertools import combinations

def find_original_set(sets):
    original_set = set()
    for size in range(len(sets)):
        for subset in combinations(sets, size):
            subset_union = set().union(*subset)
            if len(subset_union) == size:
                original_set = subset_union
                break
    return original_set