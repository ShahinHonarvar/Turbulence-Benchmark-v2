def find_original_set(*args):
    if len(args) != 845:
        raise TypeError('Exactly 845 arguments are required')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
    return set.union(*args)