def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Exactly 63 arguments are required')
    if len(set(map(id, args))) != 63:
        raise ValueError('All 63 arguments must be distinct')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        if not arg.issubset(set(map(int, arg))):
            raise ValueError('All sets must contain only integers')
        original_set.update(arg)
    return original_set