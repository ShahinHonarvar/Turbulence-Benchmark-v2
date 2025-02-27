def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise TypeError('All elements of the sets must be integers')
    if len(set((frozenset(arg) for arg in args))) != 96:
        raise ValueError('All sets must be distinct')
    result = set()
    for arg in args:
        result.update(arg)
    return result