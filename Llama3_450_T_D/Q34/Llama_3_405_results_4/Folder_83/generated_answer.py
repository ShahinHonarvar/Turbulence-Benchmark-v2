def find_original_set(*args):
    if len(args) != 64:
        raise TypeError('find_original_set expected 64 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('all arguments to find_original_set must be sets of integers')
    return set.union(*args)