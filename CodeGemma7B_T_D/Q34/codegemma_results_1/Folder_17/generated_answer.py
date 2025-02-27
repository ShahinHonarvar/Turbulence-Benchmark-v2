from itertools import combinations

def find_original_set(lists):
    combos = combinations(lists, 1)
    size_combos = sorted(combos, key=len)
    return size_combos[0][0]