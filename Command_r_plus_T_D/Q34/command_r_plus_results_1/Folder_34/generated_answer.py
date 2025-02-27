def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Function must be called with exactly 95 arguments.')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in sets must be integers.')
    original_set = set.union(*args)
    return original_set