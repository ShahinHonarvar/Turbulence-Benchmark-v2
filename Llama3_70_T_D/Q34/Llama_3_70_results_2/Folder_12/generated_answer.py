def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Exactly 51 arguments are required')
    if len(set(map(id, args))) != len(args):
        raise ValueError('All arguments must be distinct')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('Each argument must be a set of integers')
    return set.union(*args)