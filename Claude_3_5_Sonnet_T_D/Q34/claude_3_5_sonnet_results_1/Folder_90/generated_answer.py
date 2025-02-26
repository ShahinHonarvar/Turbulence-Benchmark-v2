def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('Function requires exactly 985 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
    return set.union(*args)