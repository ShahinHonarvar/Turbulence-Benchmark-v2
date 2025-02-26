def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function must be called with exactly 990 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    if len(set(map(frozenset, args))) != 990:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)