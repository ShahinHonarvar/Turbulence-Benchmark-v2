def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('Function requires exactly 478 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    if len(set((frozenset(arg) for arg in args))) != 478:
        raise ValueError('All arguments must be distinct')
    return set().union(*args)