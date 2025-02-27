def find_original_set(*args):
    if len(args) != 828:
        raise TypeError('find_original_set expected 828 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('all arguments must be sets')
    return set.union(*args)