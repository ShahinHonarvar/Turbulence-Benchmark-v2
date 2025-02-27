def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('Exactly 45 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(elem, int) for arg in args for elem in arg)):
        raise ValueError('All set elements must be integers')
    if len(args) != len(set((frozenset(arg) for arg in args))):
        raise ValueError('All arguments must be distinct')
    return set.union(*args)