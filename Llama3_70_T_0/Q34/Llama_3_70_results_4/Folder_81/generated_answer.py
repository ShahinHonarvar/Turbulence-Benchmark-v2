def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Exactly 72 arguments are required')
    if len(set(map(frozenset, args))) != 72:
        raise ValueError('All arguments must be distinct')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set