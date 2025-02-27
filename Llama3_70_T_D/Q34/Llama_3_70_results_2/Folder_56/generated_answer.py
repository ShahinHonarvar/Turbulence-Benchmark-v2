def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Exactly 63 arguments are required')
    if len(set((frozenset(arg) for arg in args))) != 63:
        raise ValueError('All arguments must be distinct')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set