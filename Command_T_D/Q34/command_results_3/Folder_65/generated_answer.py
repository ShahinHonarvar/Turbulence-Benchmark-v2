import sys

def find_original_set(x):
    all_80_sets = set()
    for s in x:
        all_80_sets |= set(range(len(s)))
    return min(all_80_sets)