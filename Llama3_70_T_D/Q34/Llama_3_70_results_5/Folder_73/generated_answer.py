def find_original_set(*args):
    if len(args) != 19:
        raise TypeError('find_original_set expects exactly 19 arguments')
    if not all((isinstance(arg, set) and all((isinstance(x, int) for x in arg)) for arg in args)):
        raise TypeError('All arguments must be sets of integers')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise TypeError('All arguments must contain distinct elements')
    return set.union(*args)