def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Function requires exactly 56 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
    if len(set((frozenset(arg) for arg in args))) != 56:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)