def find_original_set(*args):
    if len(args) != 9:
        raise ValueError('Function requires exactly 9 arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(item, int) for item in arg)):
            raise TypeError('All elements in sets must be integers')
    if len(set(map(frozenset, args))) != 9:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)