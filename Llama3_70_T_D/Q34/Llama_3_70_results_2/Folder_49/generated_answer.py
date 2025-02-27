def find_original_set(*args):
    if len(args) != 60:
        raise TypeError('Exactly 60 arguments are required')
    if len(set((frozenset(arg) for arg in args))) != 60:
        raise TypeError('All arguments must be distinct')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise TypeError('All arguments must be sets of integers')
    return set.union(*args)