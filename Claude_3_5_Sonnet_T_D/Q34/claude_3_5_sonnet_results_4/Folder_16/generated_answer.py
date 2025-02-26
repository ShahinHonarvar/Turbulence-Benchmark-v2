def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('Function requires exactly 321 arguments')
    unique_args = set((frozenset(arg) for arg in args))
    if len(unique_args) != 321:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)