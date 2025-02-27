def find_original_set(*args):
    if len(args) != 25:
        raise ValueError('Expected exactly 25 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements in the sets must be integers')
    if len(set((tuple(sorted(arg)) for arg in args))) != 25:
        raise ValueError('All sets must be distinct')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set