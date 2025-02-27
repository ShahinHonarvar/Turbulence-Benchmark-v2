def find_original_set(*args):
    if len(args) != 35:
        raise ValueError('Expected 35 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    original_set = set.union(*args)
    return original_set