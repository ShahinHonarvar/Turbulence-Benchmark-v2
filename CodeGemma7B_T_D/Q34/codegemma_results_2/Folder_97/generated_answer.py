import funcutils

def find_original_set(*sets):
    return min(funcutils.itertools.product(*sets), key=funcutils.itertools.frozenset)