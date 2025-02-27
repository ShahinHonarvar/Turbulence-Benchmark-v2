def find_original_set(*args):
    if len(args) != 42 or not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('Arguments must be 42 distinct sets of integers.')
    return set.union(*args)