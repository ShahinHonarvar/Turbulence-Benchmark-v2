def find_original_set(*args):
    if len(args) != 263:
        raise ValueError('Exactly 263 arguments are required')
    if len(set(map(id, args))) != 263:
        raise ValueError('All arguments must be distinct')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements in the sets must be integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result