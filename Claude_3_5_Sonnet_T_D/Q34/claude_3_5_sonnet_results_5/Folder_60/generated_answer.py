def find_original_set(*args):
    if len(args) != 35:
        raise ValueError('Function requires exactly 35 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    if len(set(map(frozenset, args))) != 35:
        raise ValueError('All argument sets must be distinct')
    return set().union(*args)