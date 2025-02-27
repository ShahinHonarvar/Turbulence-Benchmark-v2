def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Function must take exactly 60 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise ValueError('All elements in sets must be integers')
    return set.union(*args)