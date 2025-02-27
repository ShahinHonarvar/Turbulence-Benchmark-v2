def find_original_set(*args):
    if len(args) != 849:
        raise TypeError('find_original_set expected 849 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('all arguments must be sets')
    original_set = set.union(*args)
    return original_set