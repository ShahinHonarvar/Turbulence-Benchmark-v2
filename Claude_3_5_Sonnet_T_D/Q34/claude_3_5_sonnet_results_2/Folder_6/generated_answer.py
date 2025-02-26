def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Function must receive exactly 276 arguments')
    unique_sets = set((frozenset(arg) for arg in args))
    if len(unique_sets) != 276:
        raise ValueError('All 276 arguments must be distinct sets')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set