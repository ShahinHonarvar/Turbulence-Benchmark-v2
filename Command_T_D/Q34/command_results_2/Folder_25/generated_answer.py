import itertools

def find_original_set(X):
    original_sets = set(itertools.chain.from_iterable(itertools.permutations(X)))
    return min(original_sets, key=lambda x: x)