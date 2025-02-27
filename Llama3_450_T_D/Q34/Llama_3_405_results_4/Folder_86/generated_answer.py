def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Exactly 162 arguments are required')
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
    return set.union(*args)