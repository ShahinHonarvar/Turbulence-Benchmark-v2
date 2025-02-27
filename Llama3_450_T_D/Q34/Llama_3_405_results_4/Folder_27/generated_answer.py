def find_original_set(*args):
    if len(args) != 100:
        raise ValueError('Exactly 100 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    return set.union(*args)