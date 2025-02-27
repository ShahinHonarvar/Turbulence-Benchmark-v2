def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Exactly 42 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All elements in the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 42:
        raise ValueError('All sets must be distinct')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set