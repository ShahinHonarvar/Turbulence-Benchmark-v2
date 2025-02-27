def find_original_set(*args):
    if len(args) != 926:
        raise TypeError('find_original_set expected 926 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    return set.union(*args)