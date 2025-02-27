def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('Expected 415 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
    return set.union(*args)