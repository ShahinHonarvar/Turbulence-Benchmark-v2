def find_original_set(*args):
    if len(args) != 162:
        raise TypeError('find_original_set expected 162 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments must be sets')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise TypeError('all sets must contain distinct integers')
    return set.union(*args)