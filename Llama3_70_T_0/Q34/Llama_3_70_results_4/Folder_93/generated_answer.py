def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Exactly 90 arguments are required')
    if len(set(map(frozenset, args))) != 90:
        raise ValueError('All arguments must be distinct')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set