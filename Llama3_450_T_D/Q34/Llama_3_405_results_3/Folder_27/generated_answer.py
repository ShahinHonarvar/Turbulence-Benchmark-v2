def find_original_set(*args):
    if len(args) != 100:
        raise TypeError('find_original_set expected 100 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise TypeError('All sets must contain distinct integers')
    return set.union(*args)