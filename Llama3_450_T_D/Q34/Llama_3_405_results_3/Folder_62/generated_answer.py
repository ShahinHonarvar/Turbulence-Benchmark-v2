def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((len(set(arg)) == len(arg) for arg in args)):
        raise ValueError('All arguments must be distinct')
    return set.union(*args)