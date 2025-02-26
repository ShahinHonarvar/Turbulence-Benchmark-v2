def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Function must be called with exactly 49 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    if len(set((frozenset(arg) for arg in args))) != 49:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)