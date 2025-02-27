from itertools import combinations

def find_original_set(sets):
    max_set = max(sets, key=len)
    for i in range(len(max_set)):
        for subset in combinations(max_set, i + 1):
            if all((s <= subset for s in sets)):
                return subset