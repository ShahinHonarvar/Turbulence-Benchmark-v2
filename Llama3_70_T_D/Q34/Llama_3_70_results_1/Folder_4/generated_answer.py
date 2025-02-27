def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Exactly 40 arguments are required')
    if len(set(map(frozenset, args))) != 40:
        raise ValueError('All arguments must be distinct')
    result = set()
    for s in args:
        result.update(s)
    return result