def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 arguments are required')
    if len(set(map(frozenset, args))) != 85:
        raise ValueError('All arguments must be distinct')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    result = set()
    for arg in args:
        result = result.union(arg)
    return result