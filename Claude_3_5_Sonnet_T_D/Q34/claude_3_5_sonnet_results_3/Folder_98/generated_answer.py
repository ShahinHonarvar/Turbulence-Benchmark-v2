def find_original_set(*args):
    if len(args) != 9:
        raise ValueError('Function requires exactly 9 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    if len(set(map(frozenset, args))) != 9:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)