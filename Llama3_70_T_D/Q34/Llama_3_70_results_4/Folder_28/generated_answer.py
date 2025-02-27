def find_original_set(*args):
    if len(args) != 43:
        raise ValueError('Exactly 43 distinct arguments are required')
    if not all((isinstance(arg, set) and arg for arg in args)):
        raise ValueError('Each argument must be a non-empty set of integers')
    if not all((not any((arg & other for other in args[i + 1:])) for i, arg in enumerate(args))):
        raise ValueError('Arguments must be distinct')
    return set.union(*args)