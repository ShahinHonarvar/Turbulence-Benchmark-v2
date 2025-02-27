from itertools import combinations

def find_original_set(sets):
    target_set = set()
    for subset in combinations(sets, len(sets)):
        if all((s.issubset(subset) for s in sets)):
            target_set = subset
    return target_set