def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Exactly 48 distinct sets are required')
    if any((not isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if any((not isinstance(x, int) for arg in args for x in arg)):
        raise ValueError('All elements in the sets must be integers')
    if len(set((tuple(sorted(arg)) for arg in args))) != 48:
        raise ValueError('All sets must be distinct')
    result = set()
    for arg in args:
        result.update(arg)
    return result