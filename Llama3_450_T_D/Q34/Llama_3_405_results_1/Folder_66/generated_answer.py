def find_original_set(*args):
    if len(args) != 25:
        raise TypeError('Expected 25 arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
    return set.union(*args)