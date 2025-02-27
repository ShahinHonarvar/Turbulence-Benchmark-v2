def find_original_set(*args):
    if len(args) != 94:
        raise ValueError('Function requires exactly 94 arguments.')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in sets must be integers.')
    original_set = set.union(*args)
    return original_set