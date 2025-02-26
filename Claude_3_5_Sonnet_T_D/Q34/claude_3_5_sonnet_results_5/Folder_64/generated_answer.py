def find_original_set(*args):
    if len(args) != 7:
        raise ValueError('Function requires exactly 7 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All set elements must be integers')
    if len(set((frozenset(arg) for arg in args))) != 7:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)