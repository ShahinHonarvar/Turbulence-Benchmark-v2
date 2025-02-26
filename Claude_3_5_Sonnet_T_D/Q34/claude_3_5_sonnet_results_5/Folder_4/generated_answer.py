def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Function expects exactly 40 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    if len(set(map(frozenset, args))) != 40:
        raise ValueError('All arguments must be distinct sets')
    return set().union(*args)