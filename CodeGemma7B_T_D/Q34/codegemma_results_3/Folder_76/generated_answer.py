from itertools import combinations

def find_original_set(sets):
    min_set = set(range(max([max(s) for s in sets]) + 1))
    for comb in combinations(min_set, len(sets)):
        if all((s <= comb for s in sets)):
            return comb