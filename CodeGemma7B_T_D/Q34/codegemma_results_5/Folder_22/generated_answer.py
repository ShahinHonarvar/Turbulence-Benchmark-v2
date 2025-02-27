import itertools

def find_original_set(*sets):
    return min(itertools.product(*sets), key=len)