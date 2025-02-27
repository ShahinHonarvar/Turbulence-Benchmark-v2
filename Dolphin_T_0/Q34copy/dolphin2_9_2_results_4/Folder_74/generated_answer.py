import itertools

def find_original_set(*sets):
    return min(set(itertools.chain.from_iterable(sets)))