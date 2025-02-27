def find_original_set(*args):
    if len(args) != 94:
        raise TypeError('find_original_set expected 94 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise TypeError('All set elements must be integers')
    return set.union(*args)