def find_original_set(*args):
    if len(args) != 80:
        raise ValueError('Function requires exactly 80 arguments')
    unique_sets = set((frozenset(arg) for arg in args))
    if len(unique_sets) != 80:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)