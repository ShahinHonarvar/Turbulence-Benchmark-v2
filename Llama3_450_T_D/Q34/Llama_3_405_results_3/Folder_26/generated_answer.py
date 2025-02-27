def find_original_set(*args):
    if len(args) != 632:
        raise ValueError('Exactly 632 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    return set.union(*args)