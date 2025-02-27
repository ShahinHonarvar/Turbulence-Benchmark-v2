def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Exactly 95 arguments are required')
    if len(set(map(frozenset, args))) != 95:
        raise ValueError('All arguments must be distinct')
    result = set()
    for s in args:
        result.update(s)
    return result