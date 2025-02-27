def find_original_set(*args):
    if len(args) != 85:
        raise TypeError('find_original_set expected 85 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('find_original_set expected sets, got {}'.format(type(arg)))
    return set.union(*args)