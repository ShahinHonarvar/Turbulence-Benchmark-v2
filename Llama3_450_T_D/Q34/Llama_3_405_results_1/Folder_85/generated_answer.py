def find_original_set(*args):
    if len(args) != 85:
        raise TypeError('find_original_set expected 85 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments must be sets')
    return set.union(*args)