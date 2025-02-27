def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 arguments are required.')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in sets must be integers.')
    if not all((s for s in args)):
        raise ValueError('All sets must be non-empty.')
    original_set = set.union(*args)
    return original_set