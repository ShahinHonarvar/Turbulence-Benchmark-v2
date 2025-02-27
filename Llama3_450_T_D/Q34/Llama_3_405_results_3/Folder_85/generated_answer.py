def find_original_set(*args):
    if len(args) != 85:
        raise TypeError('find_original_set expected 85 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise TypeError('all set elements must be integers')
    return set.union(*args)