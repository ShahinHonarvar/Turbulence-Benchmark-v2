def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Exactly 714 arguments are required.')
    if not all((isinstance(arg, set) and all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set.union(*args)
    return original_set