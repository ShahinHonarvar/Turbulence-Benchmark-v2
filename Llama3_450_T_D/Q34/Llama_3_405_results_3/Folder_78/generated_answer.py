def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Exactly 48 sets must be provided')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    return set.union(*args)