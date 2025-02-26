def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Function must receive exactly 132 arguments')
    unique_sets = set((frozenset(arg) for arg in args))
    if len(unique_sets) != 132:
        raise ValueError('All arguments must be distinct sets')
    return set().union(*args)