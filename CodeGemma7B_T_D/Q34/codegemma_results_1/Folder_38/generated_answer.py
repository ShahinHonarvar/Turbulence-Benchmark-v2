from itertools import combinations

def find_original_set(sets):
    orig_set = set()
    for size in range(len(sets)):
        for subset in combinations(sets, size):
            if all((s.issubset(subset) for s in sets)):
                orig_set = subset
    return orig_set