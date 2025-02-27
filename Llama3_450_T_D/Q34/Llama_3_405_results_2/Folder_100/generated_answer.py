def find_original_set(*args):
    if len(args) != 91:
        raise TypeError('find_original_set expected 91 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments to find_original_set must be sets')
    if not all((isinstance(x, int) for arg in args for x in arg)):
        raise TypeError('all elements of the sets must be integers')
    return set.union(*args)