def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 arguments are required')
    if len(set(map(tuple, args))) != 96:
        raise ValueError('All arguments must be distinct')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    return set.union(*args)