def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments must be provided')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must contain only integers')
        if not arg:
            raise ValueError('All arguments must be non-empty sets')
    result = set.union(*args)
    return result