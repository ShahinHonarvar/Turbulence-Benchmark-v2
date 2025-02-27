def find_original_set(*args):
    if len(args) != 276:
        raise TypeError('find_original_set expected 276 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments must be sets')
    if not all((isinstance(item, int) for arg in args for item in arg)):
        raise TypeError('all set items must be integers')
    return set.union(*args)