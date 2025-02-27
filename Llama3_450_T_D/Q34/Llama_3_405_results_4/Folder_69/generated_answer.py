def find_original_set(*args):
    if len(args) != 126:
        raise TypeError('find_original_set expected 126 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('find_original_set expected sets, got {}'.format(type(arg)))
    return set.union(*args)