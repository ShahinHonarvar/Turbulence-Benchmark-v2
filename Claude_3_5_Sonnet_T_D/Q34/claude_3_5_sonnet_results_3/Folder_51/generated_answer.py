def find_original_set(*args):
    if len(args) != 28:
        raise ValueError('Function must have exactly 28 arguments')
    if any((not isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if any((not all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All set elements must be integers')
    if len(set(map(frozenset, args))) != 28:
        raise ValueError('All arguments must be distinct sets')
    return set().union(*args)