def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Function requires exactly 459 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    return set.union(*args)