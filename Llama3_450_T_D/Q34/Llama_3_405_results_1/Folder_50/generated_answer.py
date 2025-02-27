def find_original_set(*args):
    if len(args) != 99:
        raise TypeError('find_original_set expected 99 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments to find_original_set must be sets')
    return set.union(*args)