def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Exactly 132 arguments are required')
    if len(set(map(id, args))) != 132:
        raise ValueError('All arguments must be distinct')
    if not all((isinstance(arg, set) and arg.issubset(range(-2 ** 31, 2 ** 31)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    return set.union(*args)