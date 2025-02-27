from itertools import combinations

def find_original_set(*args):
    return min(set.union(*args))