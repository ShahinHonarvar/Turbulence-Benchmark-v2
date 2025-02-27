def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Incorrect number of arguments.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('Expected set of integers.')
    min_set = min(args, key=len)
    return min_set