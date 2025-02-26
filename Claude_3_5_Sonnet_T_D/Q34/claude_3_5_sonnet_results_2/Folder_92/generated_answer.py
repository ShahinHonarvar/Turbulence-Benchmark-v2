def find_original_set(*args):
    if len(args) != 8:
        raise ValueError('Function must receive exactly 8 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All elements in the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 8:
        raise ValueError('All arguments must be distinct sets')
    return set.union(*args)