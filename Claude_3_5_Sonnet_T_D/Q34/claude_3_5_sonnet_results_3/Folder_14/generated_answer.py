def find_original_set(*args):
    if len(args) != 13:
        raise ValueError('Function requires exactly 13 arguments')
    if any((not isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if any((not all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All set elements must be integers')
    if len(set((frozenset(arg) for arg in args))) != 13:
        raise ValueError('All arguments must be distinct sets')
    return set().union(*args)